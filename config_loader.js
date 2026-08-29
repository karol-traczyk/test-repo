#!/usr/bin/env node
/**
 * Configuration Loader (JavaScript/Node.js version)
 * Demonstrates how to load region configuration from environment variables and config files.
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class ConfigLoader {
  /**
   * Load and manage application configuration with region settings.
   * @param {string} configFile - Path to the configuration file
   */
  constructor(configFile = 'config.yaml') {
    this.configFile = configFile;
    this.config = this._loadConfig();
  }

  /**
   * Load configuration from YAML file.
   * @private
   */
  _loadConfig() {
    try {
      const filePath = path.resolve(this.configFile);
      const fileContents = fs.readFileSync(filePath, 'utf8');
      return yaml.load(fileContents);
    } catch (e) {
      throw new Error(`Failed to load configuration file: ${e.message}`);
    }
  }

  /**
   * Get the configured region.
   * Priority: Environment variable > Config file
   * @returns {string} The configured region
   */
  getRegion() {
    // Check environment variable first
    const envRegion = process.env.AWS_REGION;
    if (envRegion) {
      console.log(`Using region from environment variable: ${envRegion}`);
      return envRegion;
    }

    // Fall back to config file
    const configRegion = this.config?.region?.primary || 'us-east-1';
    console.log(`Using region from config file: ${configRegion}`);
    return configRegion;
  }

  /**
   * Get detailed information about a region.
   * @param {string|null} region - Region to get info for (defaults to current region)
   * @returns {object} Region information
   */
  getRegionInfo(region = null) {
    if (!region) {
      region = this.getRegion();
    }

    const regionSettings = this.config?.region?.settings || {};
    return regionSettings[region] || {};
  }

  /**
   * List all available regions from config.
   * @returns {string[]} Array of available region codes
   */
  listAvailableRegions() {
    const regionSettings = this.config?.region?.settings || {};
    return Object.entries(regionSettings)
      .filter(([_, info]) => info.enabled)
      .map(([region, _]) => region);
  }

  /**
   * Get the application environment.
   * @returns {string} The current environment
   */
  getEnvironment() {
    return process.env.ENVIRONMENT || 'development';
  }
}

/**
 * Example usage of ConfigLoader.
 */
function main() {
  console.log('='.repeat(60));
  console.log('Region Configuration Loader');
  console.log('='.repeat(60));

  try {
    const config = new ConfigLoader();

    // Display current region
    const currentRegion = config.getRegion();
    console.log(`\n✓ Current Region: ${currentRegion}`);

    // Display region details
    const regionInfo = config.getRegionInfo();
    if (Object.keys(regionInfo).length > 0) {
      console.log(`  Name: ${regionInfo.name || 'N/A'}`);
      console.log(`  Availability Zones: ${regionInfo.availability_zones || 'N/A'}`);
    }

    // Display environment
    console.log(`\n✓ Environment: ${config.getEnvironment()}`);

    // List available regions
    console.log('\n✓ Available Regions:');
    config.listAvailableRegions().forEach(region => {
      const info = config.getRegionInfo(region);
      console.log(`  - ${region}: ${info.name || 'N/A'}`);
    });

    console.log('\n' + '='.repeat(60));
    console.log('To change the region, set the AWS_REGION environment variable:');
    console.log('  export AWS_REGION=eu-west-1');
    console.log('  node config_loader.js');
    console.log('='.repeat(60));

    return 0;
  } catch (e) {
    console.error(`\n✗ Error: ${e.message}`);
    return 1;
  }
}

// Run if called directly
if (require.main === module) {
  process.exit(main());
}

module.exports = ConfigLoader;
