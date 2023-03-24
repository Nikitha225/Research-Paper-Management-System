const mongoose = require("mongoose");

const ParaSchema = new mongoose.Schema({
  font_size: {
    type: Number,
    required: [true, "font size not available"],
  },
  bold: {
    type: Boolean,
    required: [true, "Boolean value not available"],
  },
  text: {
    type: String,
    require: [true, "paragraph text not available"],
  },
});

module.exports = mongoose.model("Paragraph", ParaSchema);
