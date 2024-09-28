const express = require("express");
const { connectToMongoDB } = require("./database");
const cors = require("cors");

const app = express();
app.use(express.json());

app.use(
  cors({
    origin: "*",
  })
);

let db, dataColl;

async function setupMongoDB() {
  try {
    const client = await connectToMongoDB();
    db = client.db("hts");
    dataColl = db.collection("data");
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error("Error connecting to MongoDB:", error);
    process.exit(1);
  }
}

app.get("/data", async (req, res) => {
  try {
    const data = await dataColl.find({}).toArray();
    console.log("Fetched data:", data);
    res.json(data);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).json({
      message: "There was an error fetching the data.",
      error: error.message,
    });
  }
});

async function startServer() {
  await setupMongoDB();
  const port = process.env.PORT || 8000;
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}

startServer();
