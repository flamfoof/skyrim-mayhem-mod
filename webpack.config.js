const path = require('path');

module.exports = {
  // ... other webpack configuration ...

  devServer: {
    static: "build",
    port: 8080,
    server: "https",
    https: false,
    // ... other devServer settings ...
  },
};