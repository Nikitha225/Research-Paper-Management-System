const express = require("express");

const router = express.Router();

const { getAllDocs, getDoc } = require("../controllers/documents");

router.route("/").get(getAllDocs);
router.route("/:id").get(getDoc);

module.exports = router;
