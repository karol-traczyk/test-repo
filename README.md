# test-repo

A test repository with easily configurable region settings.

## 📍 Region Configuration

This project supports flexible region configuration through multiple methods. The region can be easily changed without modifying code.

### Quick Start

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` to set your desired region:**
   ```bash
   # Change the region to your preferred location
   AWS_REGION=eu-west-1
   ```

3. **Run the configuration loader:**
   ```bash
   # Python version
   pip install -r requirements.txt
   python config_loader.py
   
   # Or JavaScript/Node.js version
   npm install
   node config_loader.js
   ```

## Configuration Methods

### Method 1: Environment Variables (Recommended)

Set the `AWS_REGION` environment variable:

```bash
# Temporary (current session only)
export AWS_REGION=eu-west-1
python config_loader.py

# Or create/edit .env file
echo "AWS_REGION=eu-west-1" > .env
```

### Method 2: Config File

Edit `config.yaml` and change the `region.primary` value:

```yaml
region:
  primary: eu-west-1  # Change this to your desired region
```

**Note:** Environment variables take precedence over config file settings.

## Available Regions

The following regions are configured and available:

| Region Code | Region Name | Availability Zones |
|------------|-------------|-------------------|
| us-east-1 | US East (N. Virginia) | 6 |
| us-west-2 | US West (Oregon) | 4 |
| eu-west-1 | EU West (Ireland) | 3 |
| eu-central-1 | EU Central (Frankfurt) | 3 |
| ap-southeast-1 | Asia Pacific (Singapore) | 3 |
| ap-northeast-1 | Asia Pacific (Tokyo) | 4 |

To add more regions, edit the `region.settings` section in `config.yaml`.

## Configuration Priority

The configuration loader follows this priority order:

1. **Environment Variables** (`AWS_REGION`) - Highest priority
2. **Config File** (`config.yaml`) - Fallback
3. **Default Value** (`us-east-1`) - Last resort

## Project Structure

```
test-repo/
├── .env.example          # Example environment configuration
├── .gitignore           # Git ignore rules (excludes .env)
├── config.yaml          # Main configuration file with region settings
├── config_loader.py     # Python configuration loader
├── config_loader.js     # JavaScript configuration loader
├── requirements.txt     # Python dependencies
├── package.json         # Node.js dependencies
└── README.md           # This file
```

## Usage Examples

### Python

```python
from config_loader import ConfigLoader

# Initialize configuration
config = ConfigLoader()

# Get current region
region = config.get_region()
print(f"Current region: {region}")

# Get region details
info = config.get_region_info()
print(f"Region name: {info['name']}")

# List all available regions
regions = config.list_available_regions()
```

### JavaScript/Node.js

```javascript
const ConfigLoader = require('./config_loader');

// Initialize configuration
const config = new ConfigLoader();

// Get current region
const region = config.getRegion();
console.log(`Current region: ${region}`);

// Get region details
const info = config.getRegionInfo();
console.log(`Region name: ${info.name}`);

// List all available regions
const regions = config.listAvailableRegions();
```

### Command Line

```bash
# Use default region (from config.yaml or environment)
python config_loader.py

# Override region for this execution
AWS_REGION=ap-southeast-1 python config_loader.py

# Or for Node.js
AWS_REGION=ap-southeast-1 node config_loader.js
```

## Deployment

When deploying to different environments, you can:

1. **Set environment variables** in your deployment platform (AWS, Heroku, Docker, etc.)
2. **Use different config files** for different environments (e.g., `config.production.yaml`)
3. **Use CI/CD variables** to inject the region during deployment

### Example: Docker

```dockerfile
# Set region at build time
ENV AWS_REGION=eu-west-1

# Or override at runtime
docker run -e AWS_REGION=ap-northeast-1 your-image
```

### Example: Kubernetes

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  AWS_REGION: "eu-central-1"
```

## Multi-Region Support

To enable multi-region support:

1. Edit `config.yaml`:
   ```yaml
   region:
     primary: us-east-1
     backup: us-west-2  # Uncomment this line
   
   features:
     multi_region: true  # Change to true
     auto_failover: true  # Optional
   ```

2. The application will use the backup region for disaster recovery scenarios.

## Troubleshooting

### Region Not Recognized

If you see "Region not recognized," ensure:
- The region code is correct (see Available Regions table)
- The region is enabled in `config.yaml`
- Environment variable is properly set

### Configuration File Not Found

Ensure you're running the script from the project root directory where `config.yaml` exists.

## Contributing

To add support for additional regions:

1. Edit `config.yaml` and add the region under `region.settings`:
   ```yaml
   your-region-code:
     name: "Your Region Name"
     availability_zones: 3
     enabled: true
   ```

2. Test the configuration:
   ```bash
   AWS_REGION=your-region-code python config_loader.py
   ```

## License

MIT
