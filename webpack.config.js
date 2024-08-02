// Generated using webpack-cli https://github.com/webpack/webpack-cli

const path = require('path');

const config = {
    entry: './src/index.tsx',
    mode: 'production',
    output: {
      path: path.join(__dirname, 'dist'),
      filename: 'bundle.js'
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js']
    },
    module: {
      rules: [
        {
          test: /\.(ts|tsx)$/,
          use: 'ts-loader',
          exclude: /node_modules/
        },
        {
          test: /\.css$/,
          use: [
              'style-loader',
              'css-loader'
          ]
        }
      ]
    }
};

module.exports = () => {
    return config;
};
