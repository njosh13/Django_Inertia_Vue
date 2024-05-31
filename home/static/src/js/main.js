import { createApp, h } from "vue";
import { createInertiaApp, Head, Link } from "@inertiajs/vue3";
import "vite/modulepreload-polyfill";

// Import Bootstrap
import "bootstrap/dist/css/bootstrap.css";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.js";

let customRoute = (...args) => {
  args[0] = args[0];
  return window.reverseUrl(...args);
};

createInertiaApp({
  progress: {
    color: "#29d",
  },
  resolve: (name) => {
    const pages = import.meta.glob("./Pages/**/*.vue", { eager: true });
    return pages[`./Pages/${name}.vue`];
  },
  setup({ el, App, props, plugin }) {
    const app = createApp({ render: () => h(App, props) })
      .use(plugin, bootstrap)
      .component("Head", Head)
      .component("Link", Link)
      .mixin({ methods: { route: customRoute } });

    // Set global property for route
    app.config.globalProperties.$route = customRoute;

    // mount the app
    app.mount(el);
  },
});
