# test-repo

Refresh
Testing

## AWS Configuration

This project is configured to use AWS region: **eu-west-2** (Europe - London)

### Configuration Files

- `aws-config.json` - JSON configuration file with AWS settings
- `.env.example` - Environment variables template
- `terraform.tfvars` - Terraform variables configuration
- `main.tf` - Terraform infrastructure definition

### AWS Region

The AWS region is set to `eu-west-2` across all configuration files to ensure consistency.

### Usage

1. Copy `.env.example` to `.env` and update with your credentials:
   ```bash
   cp .env.example .env
   ```

2. For Terraform deployment:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

### Region Configuration

All AWS resources will be created in the **eu-west-2** region. To change the region, update the following files:
- `aws-config.json` - Update the `aws.region` field
- `.env.example` - Update `AWS_REGION` and `AWS_DEFAULT_REGION`
- `terraform.tfvars` - Update `aws_region` variable
- `main.tf` - Update the `aws_region` variable default value
