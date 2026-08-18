import { Link } from "react-router-dom";

const LandingNav = () => {
  return (
    <section className="flex justify-between items-center p-4 bg-gray-800 text-white">
      <div className="text-xl font-bold">Logo</div>
      <nav>
        <ul className="flex gap-4 items-center bg-gray-800 text-white">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="login">
              <button>Login</button>
            </Link>
          </li>
          <li>
            <Link to="register">
              <button>Register</button>
            </Link>
          </li>
        </ul>
      </nav>
    </section>
  );
};

export default LandingNav;
