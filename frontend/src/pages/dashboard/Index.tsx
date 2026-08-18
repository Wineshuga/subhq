import { Outlet } from "react-router-dom";
import Sidebar from "../../components/Sidebar";
import DashboardNav from "../../components/DashboardNav";

const Index = () => {
  return (
    <section className="flex">
      <Sidebar />
      <section className="flex-1">
        <DashboardNav />
        <Outlet />
      </section>
    </section>
  );
};

export default Index;
