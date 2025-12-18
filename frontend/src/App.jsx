import { useState } from "react";
import Header from "./components/Header";
import UploadCard from "./components/UploadCard";
import ResultGrid from "./components/ResultGrid";
import { uploadStatement } from "./api/api";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAnalyze() {
    if (!file) {
      setError("Please upload a PDF credit card statement to continue.");
      return;
    }

    setError("");
    setResult(null);
    setLoading(true);

    try {
      const res = await uploadStatement(file);
      setResult(res.data);
    } catch (err) {
      setError(
        "Unable to analyze this statement. Please ensure it is a valid credit card PDF."
      );
    } finally {
      setLoading(false);
    }
  }

  function handleFileSelect(selectedFile) {
    setFile(selectedFile);
    setResult(null);
    setError("");
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <Header />

      <main className="px-6 py-12">
        <div className="mx-auto max-w-6xl grid grid-cols-1 md:grid-cols-2 gap-8">

          {/* LEFT: Upload Section */}
          <div className="flex justify-center">
            <UploadCard
              file={file}
              onFileSelect={handleFileSelect}
              onAnalyze={handleAnalyze}
              loading={loading}
            />
          </div>

          {/* RIGHT: Result Section */}
          <div className="bg-white border border-gray-200 rounded-xl p-6 shadow-sm min-h-[260px]">

            {/* Empty State */}
            {!result && !loading && !error && (
              <div className="h-full flex items-center justify-center text-sm text-gray-500 text-center">
                Upload a credit card statement to view the extracted summary.
              </div>
            )}

            {/* Loading State */}
            {loading && (
              <div className="h-full flex items-center justify-center text-sm text-gray-500">
                Analyzing statement and extracting insights…
              </div>
            )}

            {/* Error State */}
            {error && !loading && (
              <div className="rounded-md border border-red-200 bg-red-50 px-4 py-3">
                <p className="text-sm text-red-700">{error}</p>
              </div>
            )}

            {/* Result */}
            {result && !loading && (
              <>
                <h2 className="mb-4 text-lg font-semibold text-gray-800">
                  Statement Summary
                </h2>
                <ResultGrid data={result} />
              </>
            )}
          </div>

        </div>
      </main>
    </div>
  );
}
