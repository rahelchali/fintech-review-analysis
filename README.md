\# FinTech App Review Analytics Pipeline — Ethiopian Banking Sector



An enterprise data engineering and natural language processing (NLP) pipeline built for \*\*Omega Consultancy\*\*. This platform programmatically extracts, cleans, analyzes, and stores user feedback from the Google Play Store for three prominent financial institutions in Ethiopia: \*\*Commercial Bank of Ethiopia (CBE)\*\*, \*\*Bank of Abyssinia (BOA)\*\*, and \*\*Dashen Bank\*\*.



The system transforms unstructured customer feedback into strategic competitive assets, addressing core consulting briefs regarding customer retention, feature request tracking, and automated complaint management.



---



\## 📁 Repository Directory Structure



```text

fintech-review-analysis/

├── .github/workflows/

│   └── unittests.yml       # Automated CI/CD execution configuration

├── data/

│   ├── raw/                # Extracted multi-bank raw store reviews

│   └── processed/          # Cleaned, formatted master reporting datasets

├── notebooks/

│   └── plots/              # Exported publication-quality stakeholder charts

├── scripts/

│   ├── db\_setup.py         # Relational database schema engine script

│   ├── schema.sql          # Data integrity database verification queries

│   └── sentiment\_analysis.py # VADER sentiment scoring and charting script

├── src/

│   ├── data\_preprocessing.py # Text normalization and consulting scenario tagging

│   └── thematic\_analysis.py # Keyword keyword extraction mapping module

└── tests/

&nbsp;   └── test\_pipeline.py    # Automated dataset structural testing layer

```



---



\## ⚙️ Core Technical Capabilities



1\. \*\*Robust Data Ingestion Layer (`scripts/scrape\_reviews.py`)\*\*: Multi-bank automated extraction handling pagination limits and regional fallback controls cleanly.

2\. \*\*Text Normalization Engine (`src/data\_preprocessing.py`)\*\*: Forcing string lower-casing, stripping special alphanumeric characters, and standardizing date sequences to `YYYY-MM-DD`.

3\. \*\*Strategic Scenario Tagging (`src/thematic\_analysis.py`)\*\*: Classifies reviews directly into operational consulting focus areas using keyword matching.

4\. \*\*VADER Sentiment Analytics (`scripts/sentiment\_analysis.py`)\*\*: Scores user emotion profiles using continuous compound arrays (-1 to +1) mapped to standard reporting thresholds.

5\. \*\*Relational PostgreSQL Engineering (`scripts/db\_setup.py`)\*\*: Deploys an automated SQLAlchemy ORM script to generate structural tables (`banks` and `reviews`) and execute bulk insertion.



---



\## 🗄️ Relational Database Schema Design



\### 1. `banks` Table (Metadata Lookup)

\* `bank\_id` (Integer, PRIMARY KEY): Auto-incrementing identifier.

\* `bank\_name` (String): Instituion acronym shorthand (`CBE`, `BOA`, `Dashen`).

\* `app\_name` (String): Full store bundle identifier description.



\### 2. `reviews` Table (Granular Review Facts)

\* `review\_id` (String, PRIMARY KEY): Play Store unique tracking token.

\* `bank\_id` (Integer, FOREIGN KEY referencing `banks.bank\_id`): Parent relational mapping.

\* `review\_text` (String): Text feedback submitted by consumers.

\* `rating` (Integer): Rating score scale (1 to 5 Stars).

\* `review\_date` (Date): Standardized calendar timestamp.

\* `sentiment\_label` (String): Evaluated emotion group (`Positive`, `Negative`, `Neutral`).

\* `sentiment\_score` (Float): Compound numerical density value.

\* `identified\_theme` (String): Extracted operational strategic category.



---



\## 🚀 Execution Instructions



\### 1. Initialize Local Environment

```bash

pip install -r requirements.txt

```



\### 2. Run Data and Analysis Pipelines

```bash

python src/data\_preprocessing.py

python src/thematic\_analysis.py

python scripts/sentiment\_analysis.py

python scripts/generate\_plots.py

```



\### 3. Run Database Insertion Pipeline

Ensure a local PostgreSQL instance is running, open terminal, and run:

```bash

"C:\\Program Files\\PostgreSQL\\18\\bin\\createdb.exe" -U postgres bank\_reviews

python scripts/db\_setup.py

```



\### 4. Execute Automated Test Suites

```bash

python -m unittest discover tests

```

---

