import { Link, useNavigate } from "react-router-dom";

function HomePage() {
  const navigate = useNavigate();

  function navigateHandler() {
    navigate("/products");
  }
  return (
    <>
      <h1>Welcome</h1>
      <p>
        Goto <Link to="products">the list of Documents</Link>
      </p>
    </>
  );
}

export default HomePage;
