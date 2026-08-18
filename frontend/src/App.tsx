import { createBrowserRouter } from "react-router-dom";
import Landing from "./pages/landing/Landing";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import LandingIndex from "./pages/landing/LandingIndex";
import Index from "./pages/dashboard/Index";
import Dashboard from "./pages/dashboard/Dashboard";

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
  {
    path: "/dashboard",
    element: <Index />,
    children: [
      {
        index: true,
        element: <Dashboard />,
      },
    ],
  },
]);
