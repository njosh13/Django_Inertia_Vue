// globals.js
import { getCurrentInstance } from "vue";

export function useGlobals() {
  const instance = getCurrentInstance();
  if (!instance) {
    throw new Error("useGlobals must be called within a setup function");
  }
  return {
    route: instance.appContext.config.globalProperties.$route,
  };
}
