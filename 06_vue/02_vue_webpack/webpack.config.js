//webpack 설정 파일
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  mode: 'development',
  entry: {
    // __dirname : 최상위 위치(entry point) like Django의 BASE_DIR
    // 여기서는 02_vue_webpack
    app: path.join(__dirname, 'src', 'main.js')
  },
  module: {
    rules: [{
        test: /\.vue$/, // 정규 표현식. '.vue' 확장자를 가진 모든 파일
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader'] // 여러개일 때는 배열로 작성
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist'),
  },
}