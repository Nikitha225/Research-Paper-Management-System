require("dotenv").config();
require("express-async-errors");
const path = require("path");

// extra security packages
const helmet = require("helmet");
const xss = require("xss-clean");

const express = require("express");
const app = express();

const connectDB = require("./db/connect");
// const authenticateUser = require("./middleware/authentication");
app.use(express.json());
app.use(helmet());
app.use(xss());

// routers
const docsRouter = require("./routes/documents");
// error handler
const notFoundMiddleware = require("./middleware/not-found");
const errorHandlerMiddleware = require("./middleware/error-handler");

app.get("/", (req, res) => {
  res.send("<h1>Research Papers Management API</h1>");
});

// routes
app.use("/api/v1/docs", docsRouter);

app.use(notFoundMiddleware);
app.use(errorHandlerMiddleware);

const port = process.env.PORT || 3000;

const start = async () => {
  try {
    await connectDB(process.env.MONGO_URI);
    app.listen(port, () =>
      console.log(`Server is listening on port ${port}...`)
    );
  } catch (error) {
    console.log(error);
  }
};

start();
