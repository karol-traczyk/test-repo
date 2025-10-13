# test-repo
Refresh

## Kubernetes (k8s) Tips

A collection of practical Kubernetes commands for daily operations and troubleshooting.

### 1. Contexts & Namespaces

Switch between clusters and namespaces efficiently:

```bash
# List all available contexts
kubectl config get-contexts

# Switch to a different context
kubectl config use-context <context-name>

# Set default namespace for current context
kubectl config set-context --current --namespace=<namespace>

# View current namespace
kubectl config view --minify -o jsonpath='{..namespace}'
```

**Tip:** Install `kubens` and `kubectx` for faster context/namespace switching.

### 2. Listing & Inspecting Resources

Query and examine cluster resources:

```bash
# List namespaces, pods, services, deployments
kubectl get ns
kubectl get pods [-A | -n <namespace>] -o wide
kubectl get svc [-A | -n <namespace>] -o wide
kubectl get deploy [-A | -n <namespace>] -o wide

# Detailed information about a specific resource
kubectl describe <resource>/<name>

# List all available API resources
kubectl api-resources

# Show resource schema and documentation
kubectl explain <resource>
kubectl explain <resource> --recursive
```

### 3. Logs, Exec, Port-forward

Debug running containers and access services:

```bash
# View container logs
kubectl logs <pod> [-c <container>] [--since=10m] [-f]

# Execute commands inside a pod
kubectl exec -it <pod> [-c <container>] -- sh

# Forward local port to a service or pod
kubectl port-forward svc/<name> 8080:80
kubectl port-forward pod/<name> 8080:80
```

### 4. Rollouts & Scale

Manage deployment rollouts and scaling:

```bash
# Check rollout status
kubectl rollout status deploy/<name>

# Rollback to previous deployment version
kubectl rollout undo deploy/<name>

# Scale deployment replicas
kubectl scale deploy/<name> --replicas=3
```

### 5. Apply, Diff, Kustomize

Declarative configuration management:

```bash
# Apply configuration from file or directory
kubectl apply -f <file-or-dir>

# Preview changes before applying
kubectl diff -f <file-or-dir>

# Build and apply Kustomize configurations
kubectl kustomize <dir> | kubectl apply -f -
```

### 6. Top, Events, Troubleshooting

Monitor resource usage and diagnose issues:

```bash
# View resource usage (requires metrics-server)
kubectl top nodes
kubectl top pods -A

# List recent cluster events sorted by timestamp
kubectl get events -A --sort-by=.lastTimestamp

# Get full resource definition for debugging
kubectl get pod <name> -o yaml | less
```

### 7. Nodes Maintenance

Safely manage node maintenance operations:

```bash
# Mark node as unschedulable
kubectl cordon <node>

# Drain node (evict pods gracefully)
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data

# Mark node as schedulable again
kubectl uncordon <node>
```

### 8. Handy Aliases

Speed up your workflow with shell aliases:

```bash
# Add to ~/.bashrc or ~/.zshrc
alias k=kubectl
complete -F __start_kubectl k
```
