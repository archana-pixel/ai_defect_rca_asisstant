import logging
import time
from app.embedding_service import EmbeddingService
from app.vector_store import VectorStore
from app.llm_service import generate_rca

# Optional import for Jira
try:
    from app.jira_service import JiraService
    JIRA_AVAILABLE = True
except ImportError:
    JIRA_AVAILABLE = False


class RCAEngine:
    def __init__(self, use_jira=False):
        logging.info("Initializing RCA Engine...")

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.use_jira = use_jira and JIRA_AVAILABLE

        if self.use_jira:
            self.jira_service = JiraService()
            logging.info("Jira integration enabled")
        else:
            logging.info("Jira integration disabled")

        logging.info("RCA Engine initialized successfully.")

    def analyze_failure(self, new_log: str):
        """
        Full RAG pipeline:
        1. Generate embedding
        2. Search similar historical defects
        3. Call LLM for RCA generation
        """
        try:
            start_time = time.time()

            logging.info("Step 1: Generating embedding for new defect...")
            embedding = self.embedding_service.generate_embedding(new_log)

            logging.info("Step 2: Searching similar historical defects...")
            similar_logs = self.vector_store.search_similar(embedding)
            logging.info(f"Retrieved {len(similar_logs)} similar defect logs.")

            logging.info("Step 3: Calling LLM for RCA generation...")
            rca_output = generate_rca(new_log, similar_logs)

            end_time = time.time()
            logging.info(f"RCA generation completed in {round(end_time - start_time, 2)} seconds.")

            return rca_output

        except Exception as e:
            logging.error("An error occurred while generating RCA", exc_info=True)
            raise e