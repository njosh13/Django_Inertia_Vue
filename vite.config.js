import { resolve } from "path";
import vue from "@vitejs/plugin-vue";
import dynamicImport from "vite-plugin-dynamic-import";

module.exports = {
  plugins: [vue(), dynamicImport()],
  root: resolve("./home/static/src"),
  base: "/static/",
  resolve: {
    extensions: [".js", ".json", ".vue"],
  },
  build: {
    outDir: resolve("./home/static/dist"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2015",
    rollupOptions: {
      input: {
        main: resolve("./home/static/src/js/main.js"),
      },
      output: {
        chunkFileNames: "./home/static/src/js/[name].js?id=[chunkhash]",
      },
    },
  },
};
