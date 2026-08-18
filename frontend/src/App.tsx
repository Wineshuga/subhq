import { createBrowserRouter } from "react-router-dom";
import Landing from "./pages/landing/Landing";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import LandingIndex from "./pages/landing/LandingIndex";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingIndex />,
    children: [
      {
        index: true,
        element: <Landing />,
      },
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "register",
        element: <Register />,
      },
    ],
  },
]);
