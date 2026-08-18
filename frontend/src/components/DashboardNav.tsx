const DashboardNav = () => {
  return (
    <div className="border-b border-gray-600 text-gray-800 p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Welcome, User</h1>

      <section className="flex items-center gap-4">
        <div className="w-10 h-10 rounded-full border-2 border-gray-600"></div>
        <button className="font-bold">Logout</button>
      </section>
    </div>
  );
};

export default DashboardNav;
