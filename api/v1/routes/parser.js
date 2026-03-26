const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class Parser {
    static parseFile(filePath) {
        if (!fs.existsSync(filePath)) {
            throw new Error(`File not found: ${filePath}`);
        }

        const ext = path.extname(filePath).toLowerCase();
        const fileContent = fs.readFileSync(filePath, 'utf8');

        switch (ext) {
            case '.json':
                return JSON.parse(fileContent);
            case '.yaml':
            case '.yml':
                return yaml.load(fileContent);
            default:
                throw new Error(`Unsupported file type: ${ext}`);
        }
    }

    static validateConfig(config, schema) {
        const { error } = schema.validate(config);
        if (error) {
            throw new Error(`Config validation failed: ${error.message}`);
        }
        return true;
    }
}

module.exports = Parser;