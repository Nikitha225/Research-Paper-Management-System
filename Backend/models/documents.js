const mongoose = require("mongoose");
const Paragraph = require("./paragraph");

const paraSchema = new mongoose.Schema({
  child: { type: mongoose.ObjectId, ref: "Paragraph" },
});

const pageSchema = new mongoose.Schema({
  children: [paraSchema],
});

const DocSchema = new mongoose.Schema({
  // pages: {
  //   type: [[[mongoose.Types.ObjectId]]],
  //   ref: "Paragraph",
  //   required: [true, "pages data not available"],
  // },
  pages: {
    children: [pageSchema],
  },
  file_name: {
    type: String,
    required: [true, "file name not available"],
  },
  title: {
    type: String,
    required: [true, "title not available"],
  },
});

module.exports = mongoose.model("Document", DocSchema);
