// merge_reports.js
const fs = require("fs");

const files = ["report_data/performance_test_summary.json", "report_data/spike_test_summary.json", "report_data/stress_test_summary.json"];
const rows = files.map((file) => {
  const data = JSON.parse(fs.readFileSync(file, "utf-8"));
  const metrics = data.metrics;
  return {
    name: file.replace("report_data/", "").replace("_summary.json", ""),
    p95: metrics.http_req_duration?.values["p(95)"]?.toFixed(2) ?? "N/A",
    failRate: (metrics.http_req_failed?.values.rate * 100).toFixed(2) ?? "N/A",
    reqs: metrics.http_reqs?.values.count ?? "N/A",
  };
});

const html = `
<html>
<head>
<style>
  body { font-family: -apple-system, "Segoe UI", sans-serif; background: #1a1c23; color: #e0e0e0; padding: 40px; }
  h1 { color: #7d64ff; }
  table { border-collapse: collapse; width: 100%; margin-top: 20px; }
  th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid #333; }
  th { background: #22242c; color: #ff6b35; }
  tr:hover { background: #22242c; }
  a { color: #ff6b35; text-decoration: none; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>K6 Performance Test Summary</h1>
<table>
  <tr><th>Test Scenario</th><th>P95 Response Time (ms)</th><th>Failure Rate (%)</th><th>Total Requests</th></tr>
  ${rows.map(r => `<tr><td>${r.name}</td><td>${r.p95}</td><td>${r.failRate}</td><td>${r.reqs}</td></tr>`).join("")}
</table>
<p>Detailed Reports: 
  <a href="report_data/performance_test_summary.html">performance</a> | 
  <a href="report_data/spike_test_summary.html">spike</a> | 
  <a href="report_data/stress_test_summary.html">stress</a>
</p>
</body>
</html>
`;

fs.writeFileSync("index.html", html);
console.log("REPORT：index.html");