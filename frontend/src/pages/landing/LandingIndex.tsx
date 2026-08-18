import { Outlet } from "react-router-dom";
import LandingNav from "../../components/LandingNav";

const LandingIndex = () => {
  return (
    <section>
      <LandingNav />
      <main>
        <Outlet />
      </main>
    </section>
  );
};

export default LandingIndex;
