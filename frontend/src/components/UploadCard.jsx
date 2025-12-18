export default function UploadCard({ file, onFileSelect, onAnalyze, loading }) {
  return (
    <div className="w-full max-w-lg bg-white rounded-xl border border-gray-200 shadow-sm p-6 mt-8">
      
      {/* Header */}
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-gray-900">
          Upload Credit Card Statement
        </h2>
        <p className="text-sm text-gray-500 mt-1">
          Upload a PDF statement to automatically detect the issuing bank and extract billing details.
        </p>
      </div>

      {/* Upload Area */}
      <label className="flex flex-col items-center justify-center w-full h-36 px-4 transition
                        border-2 border-dashed rounded-lg cursor-pointer
                        border-gray-300 bg-gray-50 hover:bg-gray-100">
        
        {!file ? (
          <>
            <svg
              className="w-9 h-9 mb-3 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>

            <p className="text-sm text-gray-600">
              <span className="font-medium text-gray-900">Click to upload</span> or drag and drop
            </p>
            <p className="text-xs text-gray-500 mt-1">PDF only · Max 5MB</p>
          </>
        ) : (
          <div className="flex items-center gap-3 bg-white px-4 py-2 rounded-md border border-gray-200">
            <span className="text-green-600 text-sm font-medium">✔</span>
            <div className="text-left">
              <p className="text-sm font-medium text-gray-900 truncate max-w-[220px]">
                {file.name}
              </p>
              <p className="text-xs text-gray-500">
                {(file.size / 1024 / 1024).toFixed(2)} MB · Click to replace
              </p>
            </div>
          </div>
        )}

        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => onFileSelect(e.target.files[0])}
          className="hidden"
        />
      </label>

      {/* Action Button */}
      <button
        onClick={onAnalyze}
        disabled={!file || loading}
        className="mt-6 w-full bg-blue-600 text-white py-2.5 rounded-md
                   text-sm font-medium transition
                   hover:bg-blue-700
                   disabled:bg-gray-300 disabled:cursor-not-allowed"
      >
        {loading ? "Analyzing statement…" : "Analyze Statement"}
      </button>

      {/* Footer */}
      <div className="mt-5 border-t pt-4 text-center">
        <p className="text-xs text-gray-500">
          Supported banks: <span className="font-medium">ICICI, HDFC, SBI, Axis, American Express</span>
        </p>
      </div>
    </div>
  );
}
