export default function ResultGrid({ data }) {
  if (!data || Object.keys(data).length === 0) return null;

  const FIELDS = [
    ["billing_cycle", "Billing Cycle"],
    ["due_date", "Payment Due Date"],
    ["statement_issue_date", "Statement Issue Date"],
    ["previous_balance", "Previous Balance"],
    ["outstanding_amount", "Total Outstanding"],
    ["minimum_due", "Minimum Due"],
    ["credit_limit", "Credit Limit"],
    ["available_credit", "Available Credit"],
    ["used_credit", "Used Credit"],
    ["reward_points", "Reward Points"],
  ];

  const formatCurrency = (v) =>
    v ? `₹${Number(v).toLocaleString("en-IN")}` : "—";

  const formatDate = (v) => {
    if (!v) return "—";
    const d = new Date(v);
    return isNaN(d) ? v : d.toLocaleDateString("en-IN", {
      day: "numeric", month: "short", year: "numeric"
    });
  };

  const formatValue = (key, v) => {
    if (!v) return "—";
    if (["previous_balance","outstanding_amount","minimum_due","credit_limit","available_credit","used_credit"].includes(key))
      return formatCurrency(v);
    if (key.includes("date")) return formatDate(v);
    if (key === "reward_points") return Number(v).toLocaleString("en-IN");
    return v;
  };

  return (
    <div className="mt-14 w-full max-w-5xl mx-auto">
      
      {/* Bank Header */}
      <div className="mb-8 text-center">
        <h2 className="text-3xl font-bold text-gray-900">{data.bank}</h2>
        <p className="text-gray-500 text-sm">Credit Card Statement Summary</p>
      </div>

      {/* Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {FIELDS.map(([key, label]) => (
          <div key={key} className="bg-white rounded-xl border p-6 shadow-sm">
            <p className="text-xs text-gray-500 uppercase">{label}</p>
            <p className="mt-2 text-xl font-semibold text-gray-900">
              {formatValue(key, data[key])}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
