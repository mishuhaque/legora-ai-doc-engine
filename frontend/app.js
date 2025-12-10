let history = [];

async function upload() {
  const file = document.getElementById("doc").files[0];
  if (!file) {
    alert("Please select a file first.");
    return;
  }

  const form = new FormData();
  form.append("file", file);

  // Call backend
  const res = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    body: form
  });

  const result = await res.json();

  // Store in local history
  history.push({
    name: file.name,
    category: result.category,
    time: new Date().toLocaleString(),
    result
  });

  // Render UI
  renderHistory();
  renderOutput(result);

  // Default tab: fields
  showTab("fields");
}

function renderHistory() {
  const table = document.getElementById("historyTable");

  table.innerHTML = `
    <tr class="bg-gray-200">
      <th class="p-2 border">File</th>
      <th class="p-2 border">Type</th>
      <th class="p-2 border">Uploaded</th>
    </tr>
    ${history.map(
      h => `
        <tr>
          <td class="p-2 border">${h.name}</td>
          <td class="p-2 border">${h.category}</td>
          <td class="p-2 border">${h.time}</td>
        </tr>
      `
    ).join("")}
  `;
}

function renderOutput(result) {
  document.getElementById("fields").innerText   = JSON.stringify(result.fields, null, 2);
  document.getElementById("workflow").innerText = JSON.stringify(result.workflow, null, 2);
  document.getElementById("rules").innerText    = JSON.stringify(result.rules, null, 2);
}

function showTab(tab) {
  document.querySelectorAll(".tab-content").forEach(el => el.classList.add("hidden"));
  document.getElementById(tab).classList.remove("hidden");
}
