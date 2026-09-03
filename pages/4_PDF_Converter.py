# =======================================================
# ----------------- 4. PDF CONVERTER SUITE --------------
# =======================================================
import streamlit as st
import streamlit.components.v1 as components
from utils import render_icon_html

  top_bar1, top_bar2 = st.columns([6, 1])
  with top_bar1:
      img_html = render_icon_html("pdf_icon.png", "pdf_converter_icon_1788371743841.jpg", size=65, glow_color="rgba(251, 146, 60, 0.4)")
      st.markdown(f"""
      <div style="display: flex; gap: 16px; align-items: center;">
          {img_html}
          <div>
              <h2 style="margin: 0; color: #f8fafc;">PDF Converter Suite</h2>
              <div style="color: #34d399; font-size: 0.85rem; font-weight: bold; margin-top: 2px;">🔒 100% SECURE CLIENT-SIDE PROCESSING</div>
              <div style="color: #94a3b8; font-size: 0.95rem;">Files are processed locally in your browser. They never touch our servers.</div>
          </div>
      </div>
      """, unsafe_allow_html=True)
  with top_bar2:
    st.page_link("omnitools_app.py", label="🏠 Back", use_container_width=True)

  st.divider()

  # Shared CSS for all HTML components to perfectly match your Dark Theme
  shared_css = """
  <style>
      body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: transparent; color: #f3f4f6; display: flex; justify-content: center; padding: 0.5rem; margin: 0; }
      .tool-container { background: #111827; border: 1px solid #374151; padding: 1.5rem; border-radius: 12px; width: 100%; max-width: 600px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
      label { display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.4rem; color: #9ca3af; }
      input[type="file"], input[type="text"], select { width: 100%; padding: 0.6rem; background: #1f2937; color: #fff; border: 1px solid #374151; border-radius: 6px; box-sizing: border-box; margin-bottom: 1rem; }
      button { background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%); color: white; border: none; padding: 0.8rem; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; transition: opacity 0.2s; }
      button:hover { opacity: 0.9; }
      #status { text-align: center; margin-top: 1rem; font-size: 0.95rem; font-weight: 600; color: #9ca3af; }
      .download-btn { display: none; background: #10b981; text-align: center; text-decoration: none; padding: 0.8rem; border-radius: 6px; color: white; font-weight: bold; margin-top: 1rem; }
      .download-btn:hover { background: #059669; }
  </style>
  """

  tab_img2pdf, tab_merge, tab_split, tab_extract = st.tabs([
      "🖼️ Images to PDF",
      "📑 Merge PDFs", 
      "✂️ Split / Extract Pages", 
      "📝 Extract Text"
  ])

  # ---------------- TAB 1: IMAGES TO PDF (CLIENT-SIDE) ----------------
  with tab_img2pdf:
      img2pdf_html = f"""
      {shared_css}
      <div class="tool-container">
          <h3 style="margin-top:0; color:#fff;">Images to Standardized PDF</h3>
          <label>Select images (JPG, PNG, WebP):</label>
          <input type="file" id="imgInput" accept="image/png, image/jpeg, image/jpg, image/webp" multiple>
          
          <div style="display: flex; gap: 10px; margin-bottom: 0.5rem;">
              <div style="flex: 1;">
                  <label>Page Size</label>
                  <select id="pageSize">
                      <option value="a4">A4 (Standard)</option>
                      <option value="letter">US Letter</option>
                      <option value="fit">Fit to Image</option>
                  </select>
              </div>
              <div style="flex: 1;">
                  <label>Orientation</label>
                  <select id="orientation">
                      <option value="auto">Auto Detect</option>
                      <option value="p">Portrait</option>
                      <option value="l">Landscape</option>
                  </select>
              </div>
              <div style="flex: 1;">
                  <label>Margins</label>
                  <select id="margins">
                      <option value="28">Small (10mm)</option>
                      <option value="0">None (Bleed)</option>
                      <option value="56">Medium (20mm)</option>
                  </select>
              </div>
          </div>
          
          <button onclick="convertImages()">🚀 Compile PDF</button>
          <div id="status"></div>
          <a id="downloadBtn" class="download-btn">⬇️ Download Compiled PDF</a>
      </div>
      
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
      <script>
          const loadImage = (file) => new Promise((resolve, reject) => {{
              const reader = new FileReader();
              reader.onload = (e) => {{
                  const img = new Image();
                  img.onload = () => resolve({{ img, dataUrl: e.target.result, type: file.type }});
                  img.onerror = reject;
                  img.src = e.target.result;
              }};
              reader.readAsDataURL(file);
          }});

          async function convertImages() {{
              const files = document.getElementById('imgInput').files;
              const status = document.getElementById('status');
              const btn = document.getElementById('downloadBtn');
              const pageSize = document.getElementById('pageSize').value;
              const orientPref = document.getElementById('orientation').value;
              const margin = parseInt(document.getElementById('margins').value);
              
              if (files.length === 0) {{ alert('Please select at least one image.'); return; }}
              
              status.innerText = "⏳ Processing images... Please wait.";
              btn.style.display = "none";
              
              try {{
                  const {{ jsPDF }} = window.jspdf;
                  let pdf = null;
                  const sizes = {{ 'a4': [595.28, 841.89], 'letter': [612, 792] }};
                  
                  for (let i = 0; i < files.length; i++) {{
                      status.innerText = `⏳ Processing image ${{i + 1}} of ${{files.length}}...`;
                      const {{ img, dataUrl, type }} = await loadImage(files[i]);
                      
                      let isLand = false;
                      if (orientPref === 'auto') isLand = img.width > img.height;
                      else if (orientPref === 'l') isLand = true;
                      
                      let format = sizes[pageSize];
                      let finalW, finalH;
                      
                      if (pageSize === 'fit') {{
                          format = [img.width, img.height];
                          isLand = img.width > img.height;
                          finalW = img.width;
                          finalH = img.height;
                      }} else {{
                          const baseW = isLand ? format[1] : format[0];
                          const baseH = isLand ? format[0] : format[1];
                          format = [baseW, baseH];
                          
                          const availW = baseW - (margin * 2);
                          const availH = baseH - (margin * 2);
                          
                          const imgAspect = img.width / img.height;
                          const targetAspect = availW / availH;
                          
                          if (imgAspect > targetAspect) {{
                              finalW = availW;
                              finalH = availW / imgAspect;
                          }} else {{
                              finalH = availH;
                              finalW = availH * imgAspect;
                          }}
                      }}
                      
                      const orientation = isLand ? 'l' : 'p';
                      
                      if (i === 0) {{
                          pdf = new jsPDF({{ orientation: orientation, unit: 'pt', format: format }});
                      }} else {{
                          pdf.addPage(format, orientation);
                      }}
                      
                      let x = pageSize === 'fit' ? 0 : margin + ((format[0] - (margin * 2) - finalW) / 2);
                      let y = pageSize === 'fit' ? 0 : margin + ((format[1] - (margin * 2) - finalH) / 2);
                      
                      const imgType = type === 'image/png' ? 'PNG' : (type === 'image/webp' ? 'WEBP' : 'JPEG');
                      pdf.addImage(dataUrl, imgType, x, y, finalW, finalH);
                  }}
                  
                  const pdfBlob = pdf.output('blob');
                  btn.href = URL.createObjectURL(pdfBlob);
                  btn.download = "OmniTools_Compiled_Images.pdf";
                  btn.style.display = "block";
                  status.innerText = "✅ Successfully compiled PDF!";
                  status.style.color = "#34d399";
              }} catch (e) {{
                  status.innerText = "❌ Error: " + e.message;
                  status.style.color = "#f87171";
              }}
          }}
      </script>
      """
      components.html(img2pdf_html, height=500)

  # ---------------- TAB 2: MERGE PDFS (CLIENT-SIDE) ----------------
  with tab_merge:
      merge_html = f"""
      {shared_css}
      <div class="tool-container">
          <h3 style="margin-top:0; color:#fff;">Merge Multiple PDFs</h3>
          <label>Select 2 or more PDF files (Order matters):</label>
          <input type="file" id="mergeInput" accept=".pdf" multiple>
          <button onclick="mergePdfs()">🚀 Merge in Browser</button>
          <div id="status"></div>
          <a id="downloadBtn2" class="download-btn">⬇️ Download Merged PDF</a>
      </div>
      <script src="https://unpkg.com/pdf-lib/dist/pdf-lib.min.js"></script>
      <script>
          async function mergePdfs() {{
              const files = document.getElementById('mergeInput').files;
              const status = document.getElementById('status');
              const btn = document.getElementById('downloadBtn2');
              
              if (files.length < 2) {{ alert('Please select at least 2 PDF files.'); return; }}
              
              status.innerText = "⏳ Merging files locally... Please wait.";
              btn.style.display = "none";
              
              try {{
                  const mergedPdf = await PDFLib.PDFDocument.create();
                  for (let i = 0; i < files.length; i++) {{
                      const arrayBuffer = await files[i].arrayBuffer();
                      const pdf = await PDFLib.PDFDocument.load(arrayBuffer);
                      const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
                      copiedPages.forEach((page) => mergedPdf.addPage(page));
                  }}
                  const pdfBytes = await mergedPdf.save();
                  const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
                  btn.href = URL.createObjectURL(blob);
                  btn.download = "OmniTools_Merged.pdf";
                  btn.style.display = "block";
                  status.innerText = "✅ Merged successfully!";
                  status.style.color = "#34d399";
              }} catch (e) {{
                  status.innerText = "❌ Error: " + e.message;
                  status.style.color = "#f87171";
              }}
          }}
      </script>
      """
      components.html(merge_html, height=350)

  # ---------------- TAB 3: SPLIT PDF (CLIENT-SIDE) ----------------
  with tab_split:
      split_html = f"""
      {shared_css}
      <div class="tool-container">
          <h3 style="margin-top:0; color:#fff;">Extract Pages</h3>
          <label>Select a PDF file:</label>
          <input type="file" id="splitInput" accept=".pdf">
          <label>Pages to extract (e.g., 1, 3-5, 8):</label>
          <input type="text" id="rangeInput" placeholder="1-3">
          <button onclick="splitPdf()">✂️ Extract Pages</button>
          <div id="status"></div>
          <a id="downloadBtn3" class="download-btn">⬇️ Download Extracted PDF</a>
      </div>
      <script src="https://unpkg.com/pdf-lib/dist/pdf-lib.min.js"></script>
      <script>
          async function splitPdf() {{
              const file = document.getElementById('splitInput').files[0];
              const rangeStr = document.getElementById('rangeInput').value;
              const status = document.getElementById('status');
              const btn = document.getElementById('downloadBtn3');
              
              if (!file || !rangeStr) {{ alert('Please select a file and enter a page range.'); return; }}
              
              status.innerText = "⏳ Extracting pages... Please wait.";
              btn.style.display = "none";
              
              try {{
                  const arrayBuffer = await file.arrayBuffer();
                  const pdf = await PDFLib.PDFDocument.load(arrayBuffer);
                  const totalPages = pdf.getPageCount();
                  
                  let pagesToExtract = new Set();
                  const parts = rangeStr.split(',');
                  for (let part of parts) {{
                      part = part.trim();
                      if (part.includes('-')) {{
                          let [start, end] = part.split('-');
                          start = parseInt(start); end = parseInt(end);
                          for (let p = start; p <= end; p++) {{
                              if (p >= 1 && p <= totalPages) pagesToExtract.add(p - 1);
                          }}
                      }} else {{
                          let p = parseInt(part);
                          if (p >= 1 && p <= totalPages) pagesToExtract.add(p - 1);
                      }}
                  }}
                  
                  if (pagesToExtract.size === 0) throw new Error("No valid pages found in range.");
                  
                  const newPdf = await PDFLib.PDFDocument.create();
                  const indices = Array.from(pagesToExtract).sort((a,b) => a-b);
                  const copiedPages = await newPdf.copyPages(pdf, indices);
                  copiedPages.forEach((page) => newPdf.addPage(page));
                  
                  const pdfBytes = await newPdf.save();
                  const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
                  btn.href = URL.createObjectURL(blob);
                  btn.download = "Extracted_" + file.name;
                  btn.style.display = "block";
                  status.innerText = `✅ Extracted ${{indices.length}} page(s) successfully!`;
                  status.style.color = "#34d399";
              }} catch (e) {{
                  status.innerText = "❌ Error: " + e.message;
                  status.style.color = "#f87171";
              }}
          }}
      </script>
      """
      components.html(split_html, height=450)

  # ---------------- TAB 4: EXTRACT TEXT (CLIENT-SIDE) ----------------
  with tab_extract:
      extract_html = f"""
      {shared_css}
      <div class="tool-container">
          <h3 style="margin-top:0; color:#fff;">Extract Raw Text</h3>
          <label>Select a PDF file to read:</label>
          <input type="file" id="textInput" accept=".pdf">
          <button onclick="extractText()">📝 Read Text from PDF</button>
          <div id="status"></div>
          <textarea id="outputArea" style="display:none; width:100%; height:150px; background:#1f2937; color:#fff; border:1px solid #374151; border-radius:6px; margin-top:1rem; padding:0.5rem;" readonly></textarea>
          <a id="downloadBtn4" class="download-btn">⬇️ Download Text File (.txt)</a>
      </div>
      
      <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
      <script>
          pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';
          
          async function extractText() {{
              const file = document.getElementById('textInput').files[0];
              const status = document.getElementById('status');
              const textArea = document.getElementById('outputArea');
              const btn = document.getElementById('downloadBtn4');
              
              if (!file) {{ alert('Please select a PDF file first.'); return; }}
              
              status.innerText = "⏳ Reading document... (This might take a moment)";
              textArea.style.display = "none";
              btn.style.display = "none";
              
              try {{
                  const arrayBuffer = await file.arrayBuffer();
                  const loadingTask = pdfjsLib.getDocument({{data: new Uint8Array(arrayBuffer)}});
                  const pdf = await loadingTask.promise;
                  let fullText = "";
                  
                  for (let i = 1; i <= pdf.numPages; i++) {{
                      status.innerText = `⏳ Extracting page ${{i}} of ${{pdf.numPages}}...`;
                      const page = await pdf.getPage(i);
                      const textContent = await page.getTextContent();
                      const pageText = textContent.items.map(item => item.str).join(" ");
                      fullText += `=== PAGE ${{i}} ===\\n${{pageText}}\\n\\n`;
                  }}
                  
                  textArea.value = fullText;
                  textArea.style.display = "block";
                  
                  const blob = new Blob([fullText], {{ type: 'text/plain' }});
                  btn.href = URL.createObjectURL(blob);
                  btn.download = file.name.replace('.pdf', '_extracted.txt');
                  btn.style.display = "block";
                  
                  status.innerText = "✅ Text extraction complete!";
                  status.style.color = "#34d399";
              }} catch (e) {{
                  status.innerText = "❌ Error reading PDF: " + e.message;
                  status.style.color = "#f87171";
              }}
          }}
      </script>
      """
      components.html(extract_html, height=550)
