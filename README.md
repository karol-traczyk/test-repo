# test-repo
Refresh
Testing

## AWS Configuration

This project is configured to use the **eu-west-2** (Europe - London) AWS region.

### Region Configuration

The default AWS region is set to `eu-west-2` across all configuration files:

- **Environment Variables**: See `.env.example` for environment variable configuration
- **JSON Configuration**: See `aws-config.json` for structured configuration
- **YAML Configuration**: See `config.yml` for infrastructure settings

### Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your AWS credentials (do not commit this file):
   ```
   AWS_REGION=eu-west-2
   AWS_DEFAULT_REGION=eu-west-2
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   ```

### Regional Resources

When working with region-specific AWS resources in eu-west-2, note:

- **S3 Buckets**: Use `eu-west-2` as the location constraint
- **EC2 AMIs**: AMI IDs are region-specific; use eu-west-2 AMIs
- **Availability Zones**: eu-west-2a, eu-west-2b, eu-west-2c
- **Regional Endpoints**: Configured in `aws-config.json`

### Migration Notes

This project has been configured to use eu-west-2 as the default region. If migrating existing resources:

1. Ensure all AWS resources are created in or migrated to eu-west-2
2. Update any hardcoded ARNs to use eu-west-2 format
3. Copy S3 data cross-region if needed
4. Update AMI references for EC2 instances
5. Verify regional service availability in eu-west-2
