# test-repo
Refresh

## Kubernetes

This guide covers deploying and operating the application on Kubernetes, from local development to production-ready configurations.

### Quick Start (Local Clusters)

For local development and testing, you can use **kind** or **k3d** to run Kubernetes on your machine.

#### kind (Kubernetes in Docker)

```bash
# Create a local cluster
kind create cluster --name app-dev

# Load a local image into the cluster
docker build -t <REGISTRY>/<IMAGE>:dev .
kind load docker-image <REGISTRY>/<IMAGE>:dev --name app-dev
```

#### k3d (Lightweight k3s in Docker)

```bash
# Create a local cluster
k3d cluster create app-dev

# Import a local image
docker build -t <REGISTRY>/<IMAGE>:dev .
k3d image import <REGISTRY>/<IMAGE>:dev -c app-dev
```

Both tools provide a quick way to test Kubernetes manifests locally before deploying to shared environments.

---

### Container Image and Tagging

Build and push your Docker image with consistent tagging for version control and traceability.

#### Build and Push

```bash
# Build the image
docker build -t <REGISTRY>/<IMAGE>:<TAG> .

# Push to registry (Docker Hub, GCR, ECR, etc.)
docker push <REGISTRY>/<IMAGE>:<TAG>
```

#### Recommended Tag Conventions

- `:dev` – local development
- `:main` or `:latest` – latest from the main branch
- `:<git-sha>` – specific commit (e.g., `:a1b2c3d`)
- `:v1.2.3` – semantic versioning for releases

Example:
```bash
export GIT_SHA=$(git rev-parse --short HEAD)
docker build -t myregistry/myapp:${GIT_SHA} .
docker push myregistry/myapp:${GIT_SHA}
```

---

### Base Manifests and Helm

#### Minimal Deployment and Service

A basic Kubernetes Deployment with readiness/liveness probes and resource limits:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: <REGISTRY>/<IMAGE>:<TAG>
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: ENV
          value: "production"
        - name: LOG_LEVEL
          value: "info"
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP
```

Apply the manifest:
```bash
kubectl apply -f deployment.yaml
```

#### Ingress Example

Expose your service via HTTP/HTTPS with an Ingress (requires an Ingress Controller like nginx-ingress or Traefik):

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: "letsencrypt-prod"  # Optional: for automatic TLS
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp
            port:
              number: 80
```

#### Helm Chart

Package your application with Helm for easier templating and upgrades.

**values.yaml** example:
```yaml
image:
  repository: <REGISTRY>/<IMAGE>
  tag: "latest"
  pullPolicy: IfNotPresent

replicaCount: 2

resources:
  requests:
    memory: "128Mi"
    cpu: "100m"
  limits:
    memory: "256Mi"
    cpu: "500m"

env:
  - name: ENV
    value: "production"
  - name: LOG_LEVEL
    value: "info"

service:
  type: ClusterIP
  port: 80
  targetPort: 8080

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: myapp.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: myapp-tls
      hosts:
        - myapp.example.com
```

Deploy with Helm:
```bash
# Install or upgrade the release
helm upgrade --install myapp ./helm-chart -f values.yaml

# Override values on the fly
helm upgrade --install myapp ./helm-chart \
  --set image.tag=v1.2.3 \
  --set replicaCount=3
```

---

### Configuration and Secrets

#### ConfigMap (Non-sensitive Configuration)

Store application configuration in a ConfigMap:

```bash
# Create from literals
kubectl create configmap myapp-config \
  --from-literal=LOG_LEVEL=debug \
  --from-literal=FEATURE_FLAG=enabled
```

Or from a YAML manifest:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  LOG_LEVEL: "debug"
  FEATURE_FLAG: "enabled"
  config.json: |
    {
      "timeout": 30,
      "retries": 3
    }
```

Reference in your Deployment:
```yaml
env:
- name: LOG_LEVEL
  valueFrom:
    configMapKeyRef:
      name: myapp-config
      key: LOG_LEVEL
```

#### Secret (Sensitive Data)

Store credentials and tokens securely:

```bash
# Create from literals
kubectl create secret generic myapp-secrets \
  --from-literal=DB_PASSWORD=supersecret \
  --from-literal=API_KEY=abc123xyz
```

Or from a YAML manifest (base64-encoded values):
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secrets
type: Opaque
data:
  DB_PASSWORD: c3VwZXJzZWNyZXQ=  # base64 encoded
  API_KEY: YWJjMTIzeHl6          # base64 encoded
```

Reference in your Deployment:
```yaml
env:
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: myapp-secrets
      key: DB_PASSWORD
```

**Note:** For production, consider using external secret management tools like [sealed-secrets](https://github.com/bitnami-labs/sealed-secrets), [external-secrets](https://external-secrets.io/), or cloud provider solutions (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault).

---

### Scaling and Autoscaling

#### Manual Scaling

```bash
# Scale to 5 replicas
kubectl scale deployment myapp --replicas=5

# Or via Helm
helm upgrade myapp ./helm-chart --set replicaCount=5
```

#### Horizontal Pod Autoscaler (HPA)

Automatically scale based on CPU or memory usage:

```bash
# Enable HPA based on CPU
kubectl autoscale deployment myapp \
  --cpu-percent=70 \
  --min=2 \
  --max=10
```

Or define in YAML:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

Apply:
```bash
kubectl apply -f hpa.yaml
```

**Prerequisites:** Ensure the [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) is installed in your cluster.

---

### Observability and Troubleshooting

#### Logging

Stream logs from your pods:
```bash
# Follow logs for a specific pod
kubectl logs -f <pod-name>

# Logs from all pods in a deployment
kubectl logs -f deployment/myapp

# Logs from a specific container in a multi-container pod
kubectl logs -f <pod-name> -c <container-name>

# Previous container logs (after restart)
kubectl logs <pod-name> --previous
```

**Best Practice:** Use structured logging (JSON) for easier parsing and aggregation.

#### Metrics

Expose Prometheus-compatible metrics and annotate your pods:
```yaml
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
```

View resource usage:
```bash
# Pod resource usage
kubectl top pods

# Node resource usage
kubectl top nodes
```

Visualize metrics in **Grafana** by importing dashboards or creating custom ones.

#### Tracing

If using OpenTelemetry (OTEL), configure exporter environment variables:
```yaml
env:
- name: OTEL_EXPORTER_OTLP_ENDPOINT
  value: "http://otel-collector:4317"
- name: OTEL_SERVICE_NAME
  value: "myapp"
```

#### Common Troubleshooting Commands

```bash
# List all pods
kubectl get pods

# Detailed pod information
kubectl describe pod <pod-name>

# Execute commands inside a pod
kubectl exec -it <pod-name> -- /bin/sh

# Port-forward to access a service locally
kubectl port-forward svc/myapp 8080:80

# View cluster events
kubectl get events --sort-by='.lastTimestamp'

# Check pod resource requests/limits
kubectl describe nodes
```

---

### Network and Security

#### RBAC (Role-Based Access Control)

Grant read-only access to a namespace:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: read-only
  namespace: default
rules:
- apiGroups: ["", "apps", "batch"]
  resources: ["pods", "deployments", "jobs", "services"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-only-binding
  namespace: default
subjects:
- kind: User
  name: developer@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: read-only
  apiGroup: rbac.authorization.k8s.io
```

Apply:
```bash
kubectl apply -f rbac.yaml
```

#### NetworkPolicy

Restrict traffic to your application:

```yaml
# Default deny-all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
spec:
  podSelector: {}
  policyTypes:
  - Ingress
---
# Allow specific traffic to myapp
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-myapp-ingress
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 8080
```

#### Pod Security

Harden your pods by running as non-root and using read-only filesystems:

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 1000
  capabilities:
    drop:
    - ALL
  readOnlyRootFilesystem: true
```

If your app needs a writable directory, mount an emptyDir:
```yaml
volumeMounts:
- name: tmp
  mountPath: /tmp
volumes:
- name: tmp
  emptyDir: {}
```

#### Image Security

- **Scan images** in CI with tools like [Trivy](https://github.com/aquasecurity/trivy) or [Grype](https://github.com/anchore/grype):
  ```bash
  trivy image <REGISTRY>/<IMAGE>:<TAG>
  ```
- **Keep base images up to date** to avoid CVEs.
- Use **minimal base images** (e.g., `alpine`, `distroless`) to reduce attack surface.

---

### CI/CD Pointers

Automate building, pushing, and deploying your application with CI/CD pipelines.

#### GitHub Actions Example

**.github/workflows/deploy.yml**
```yaml
name: Build and Deploy

on:
  push:
    branches: [main]

env:
  REGISTRY: <REGISTRY>
  IMAGE: <IMAGE>

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Log in to registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ secrets.REGISTRY_USERNAME }}
        password: ${{ secrets.REGISTRY_PASSWORD }}

    - name: Build and push image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: |
          ${{ env.REGISTRY }}/${{ env.IMAGE }}:${{ github.sha }}
          ${{ env.REGISTRY }}/${{ env.IMAGE }}:latest

    - name: Set up kubectl
      uses: azure/setup-kubectl@v3
      with:
        version: 'latest'

    - name: Configure kubectl
      run: |
        echo "${{ secrets.KUBECONFIG }}" | base64 -d > kubeconfig.yaml
        export KUBECONFIG=kubeconfig.yaml

    - name: Deploy with kubectl
      run: |
        kubectl set image deployment/myapp \
          myapp=${{ env.REGISTRY }}/${{ env.IMAGE }}:${{ github.sha }} \
          --record

    # OR deploy with Helm
    - name: Deploy with Helm
      run: |
        helm upgrade --install myapp ./helm-chart \
          --set image.tag=${{ github.sha }} \
          --wait
```

**Required Secrets:**
- `REGISTRY_USERNAME` and `REGISTRY_PASSWORD` – Docker registry credentials
- `KUBECONFIG` – Base64-encoded kubeconfig file for kubectl access

#### Best Practices

- **Tag images with commit SHA** for reproducibility
- **Run security scans** before pushing images
- **Use Helm for complex deployments** with environment-specific values files
- **Implement rollback strategies** (e.g., Helm rollback or kubectl rollout undo)
- **Monitor deployments** and set up alerts for failures

---

### Additional Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [kind Documentation](https://kind.sigs.k8s.io/)
- [k3d Documentation](https://k3d.io/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
