## Making GenAI more cost-efficient and accessible with open-source LLMs

This repository demonstrates a basic workflow for utilizing a Large Language Model (LLM) with a retrieval-augmented generation (RAG) approach, as described in the article  "Making GenAI more cost-efficient and accessible with open-source LLMs: [https://agileengine.com/making-genai-more-cost-efficient-and-accessible-with-open-source-llms/](https://agileengine.com/making-genai-more-cost-efficient-and-accessible-with-open-source-llms/)" by Agile Engine. This article is available as a PDF within this repository.

**Getting Started**

1. **Clone this Repository:**
   - Use Git to clone this repository to your local machine. Open your terminal and navigate to your desired directory. Then, run the following command:

     ```bash
     git clone https://github.com/Article-Support/-Making-GenAI-more-cost-efficient-and-accessible-with-open-source-LLMs.git
     ```

2. **Set Up Virtual Environment:**
   - It's recommended to use a virtual environment to isolate project dependencies. Here's how to create one using `venv`:

     ```bash
     python -m venv .venv
     ```

     This command creates a virtual environment named `.venv` in your current directory. Activate it using the following command (replace the command based on your operating system):

     - **Windows:** `.venv\Scripts\activate`
     - **macOS/Linux:** `source .venv/bin/activate`

3. **Install Dependencies:**
   - Once your virtual environment is activated, install the required packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Download LLM Model:**
   - Choose a pre-trained LLM model for your task. This example uses the Mistral-7B-Instruct model in gguf format. 
   - Download the model file (e.g., `mistral-7b-instruct-v0.1.Q6_K.gguf`) from the Hugging Face model hub and place it in the same directory as your code (`code/`). You can find the model here: [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

**Pre-built Data (Optional):**

- If you want to skip scraping data and focus on using pre-scraped articles about Nvidia (NVDA), you can proceed directly to step 9. This assumes the scraped data is available and stored appropriately in the project.

**Using Custom Data:**

5. **Run Scraper (if using custom data):**
   - Navigate to the `code` directory.
   - Edit the `scraper.py` file to customize scraping parameters. You can modify the topic within the `get_the_news` function to focus on specific articles. Here's an example call to retrieve articles about Nvidia (replace "nvda" with your desired topic):

     ```python
     articles = get_the_news("nvda")
     ```

   - Run the scraper script:
     ```bash
     python scraper.py
     ```
     **Note:** Scraping can take some time depending on the source and data size.

6. **(Optional) Adapt Configuration:**
   - If you downloaded a different model, update the model name on line 20 of both `save_vectors.py` and `query_test.py`.

7. **Generate Embeddings:**
   - Navigate back to the `code` directory and run:
     ```bash
     python save_vectors.py
     ```
     This script generates vector representations of the scraped data.

8. **Customize Prompts:**
   - Modify lines 46 to 60 in `query_test.py` to create your desired prompts for querying the LLM.

**Using Pre-built Data:**

9. **Test Your LLM (if using pre-built data):**
   - Assuming you have the pre-built Nvidia data available, you can skip directly to this step.

   - Navigate back to the `code` directory and run:
     ```bash
     python query_test.py
     ```
     This script interacts with the LLM based on your prompts.

**Happy LLMing!**

**Further Notes:**

* This is a basic example. You may