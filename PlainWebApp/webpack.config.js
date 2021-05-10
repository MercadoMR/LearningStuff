/*
https://medium.com/jeremy-gottfrieds-tech-blog/tutorial-how-to-build-a-webpack-app-with-vanilla-js-or-react-72ca2cc7e14
*/
module.exports = {
    entry: [
      './src/index.js',
      './src/index.css'
    ],
    output: {
      path: __dirname,
      publicPath: '/',
      filename: 'bundle.js'
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "script-loader"
          }
        },
        {
          test: /\.css$/,
          use: [
            {
              loader: "style-loader"
            },
            {
              loader: "css-loader",
              options: {
                modules: true,
                importLoaders: 1,
                localIdentName: "[name]_[local]_[hash:base64]",
                sourceMap: true,
                minimize: true
              }
            }
          ]
        }
      ]
    }
  };