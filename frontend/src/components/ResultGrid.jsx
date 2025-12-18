export default function ResultGrid({ data }) {
  if (!data || Object.keys(data).length === 0) return null;

  function formatLabel(key) {
    return key
      .replaceAll("_", " ")
      .replace(/\b\w/g, (char) => char.toUpperCase());
  }

  function formatCurrency(value) {
    if (value === null || value === undefined) return "—";
    if (isNaN(value)) return value;
    return `₹${Number(value).toLocaleString("en-IN")}`;
  }

  function formatDate(value) {
    if (!value) return "—";
    const date = new Date(value);
    if (isNaN(date.getTime())) return value;
    return date.toLocaleDateString("en-IN", {
      day: "numeric",
      month: "short",
      year: "numeric",
    });
  }

  function formatValue(key, value) {
    if (value === null || value === undefined) return "—";

    if (
      ["outstanding_amount", "minimum_due", "late_fee"].includes(key)
    ) {
      return formatCurrency(value);
    }

    if (key === "due_date") {
      return formatDate(value);
    }

    if (key === "top_spending_category" && typeof value === "string") {
      return value.charAt(0).toUpperCase() + value.slice(1);
    }

    return value;
  }

  return (
    <div className="mt-12 w-full max-w-5xl">
      {/* Section Header */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-gray-900">
          Statement Summary
        </h3>
        <p className="text-sm text-gray-500 mt-1">
          The following information was parsed from the uploaded statement.
        </p>
      </div>

      {/* Result Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
        {Object.entries(data).map(([key, value]) => (
          <div
            key={key}
            className="bg-white border border-gray-200 rounded-lg p-5 shadow-sm"
          >
            <p className="text-xs uppercase tracking-wide text-gray-500">
              {formatLabel(key)}
            </p>

            <p className="mt-2 text-lg font-semibold text-gray-900">
              {formatValue(key, value)}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
