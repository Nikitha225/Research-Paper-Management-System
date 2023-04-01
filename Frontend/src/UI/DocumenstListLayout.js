import classes from "./DocumenstListLayout.module.css";

const DocumentListLayout = (props) => {
  return (
    <div className={classes.layout}>
      <p className={classes.title}>Title: {props.title}</p>
      <div>
        <p className={classes.filename}>FileName: {props.filename}</p>
        <p className={classes.pages}>Pages: {props.pages}</p>
      </div>
    </div>
  );
};

export default DocumentListLayout;
