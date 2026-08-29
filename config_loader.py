#!/usr/bin/env python3
"""
Configuration Loader
Demonstrates how to load region configuration from environment variables and config files.
"""

import os
import yaml
from pathlib import Path


class ConfigLoader:
    """Load and manage application configuration with region settings."""
    
    def __init__(self, config_file='config.yaml'):
        self.config_file = Path(config_file)
        self.config = self._load_config()
        
    def _load_config(self):
        """Load configuration from YAML file."""
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
            
        with open(self.config_file, 'r') as f:
            return yaml.safe_load(f)
    
    def get_region(self):
        """
        Get the configured region.
        Priority: Environment variable > Config file
        """
        # Check environment variable first
        env_region = os.getenv('AWS_REGION')
        if env_region:
            print(f"Using region from environment variable: {env_region}")
            return env_region
        
        # Fall back to config file
        config_region = self.config.get('region', {}).get('primary', 'us-east-1')
        print(f"Using region from config file: {config_region}")
        return config_region
    
    def get_region_info(self, region=None):
        """Get detailed information about a region."""
        if region is None:
            region = self.get_region()
        
        region_settings = self.config.get('region', {}).get('settings', {})
        return region_settings.get(region, {})
    
    def list_available_regions(self):
        """List all available regions from config."""
        region_settings = self.config.get('region', {}).get('settings', {})
        return [
            region for region, info in region_settings.items()
            if info.get('enabled', False)
        ]
    
    def get_environment(self):
        """Get the application environment."""
        return os.getenv('ENVIRONMENT', 'development')


def main():
    """Example usage of ConfigLoader."""
    print("=" * 60)
    print("Region Configuration Loader")
    print("=" * 60)
    
    try:
        config = ConfigLoader()
        
        # Display current region
        current_region = config.get_region()
        print(f"\n✓ Current Region: {current_region}")
        
        # Display region details
        region_info = config.get_region_info()
        if region_info:
            print(f"  Name: {region_info.get('name', 'N/A')}")
            print(f"  Availability Zones: {region_info.get('availability_zones', 'N/A')}")
        
        # Display environment
        print(f"\n✓ Environment: {config.get_environment()}")
        
        # List available regions
        print(f"\n✓ Available Regions:")
        for region in config.list_available_regions():
            info = config.get_region_info(region)
            print(f"  - {region}: {info.get('name', 'N/A')}")
        
        print("\n" + "=" * 60)
        print("To change the region, set the AWS_REGION environment variable:")
        print("  export AWS_REGION=eu-west-1")
        print("  python config_loader.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
