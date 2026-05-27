import axios from 'axios';

const originalCreate = axios.create;
axios.create = function (config?: any) {
  if (config?.baseURL) {
    config.baseURL = config.baseURL
      .replace(/http:\/\/localhost:8888/, '/auth')
      .replace(/http:\/\/localhost:8050/, '/bonus-service-direct')
      .replace(/http:\/\/localhost:8060/, '/flight-service-direct')
      .replace(/http:\/\/localhost:8070/, '/ticket-service-direct')
      .replace(/http:\/\/localhost:8090/, '/statistics')
      .replace(/http:\/\/localhost:8080/, '/api');
  }
  return originalCreate.call(this, config);
};

// Патчер для WebSocket
const OriginalWebSocket = window.WebSocket;
window.WebSocket = function (url: string | URL, protocols?: string | string[]) {
  if (typeof url === 'string') {
    // Заменяем ws://localhost:8888/... на ws://текущий_хост/auth/...
    url = url.replace(/localhost:8888/, window.location.host + '/auth');
  }
  return new OriginalWebSocket(url, protocols);
} as any;
(window.WebSocket as any).prototype = OriginalWebSocket.prototype;