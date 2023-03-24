const Document = require("../models/documents");
const { StatusCodes } = require("http-status-codes");
const { BadRequestError, NotFoundError } = require("../errors");
const mongoose = require("mongoose");

const getAllDocs = async (req, res) => {
  const results = await Document.find({});
  const documents = results.map((doc) => {
    return { id: doc["_id"], fileName: doc["file_name"], title: doc.title };
  });
  res.status(StatusCodes.OK).json({ documents });
};

const getDoc = async (req, res) => {
  const {
    params: { id: DocID },
  } = req;

  const document = await Document.findOne({ _id: DocID });

  res.status(StatusCodes.OK).json({ document: document.pages });
};

module.exports = { getAllDocs, getDoc };
