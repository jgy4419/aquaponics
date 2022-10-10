// spring, vue 연동 블로그 https://jhhan009.tistory.com/33
module.exports = {
    assetsDir: "static",
    outputDir: "dist",
    indexPath: './public/index.html',
    devServer: {
        // 백엔드랑 서버 맞춰주기
        proxy: "http://localhost:8000"
    },
    chainWebpack: config => {
        const svgRule = config.module.rule("svg");
        // svgRule.users.clear();
        svgRule.use("vue-svg-loader").loader("vue-svg-loader");
    }
}