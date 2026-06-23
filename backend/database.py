import sqlite3

DB_NAME = "healthcare.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            disease TEXT,
            confidence REAL
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(disease, confidence):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_history
        (disease, confidence)
        VALUES (?, ?)
    """, (disease, confidence))

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM prediction_history
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_analytics():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    # Total predictions
    cursor.execute("""
        SELECT COUNT(*)
        FROM prediction_history
    """)

    total_predictions = cursor.fetchone()[0]

    # Most common disease
    cursor.execute("""
        SELECT disease,
               COUNT(*) as count
        FROM prediction_history
        GROUP BY disease
        ORDER BY count DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    most_common_disease = result[0] if result else "None"

    # Average confidence
    cursor.execute("""
        SELECT AVG(confidence)
        FROM prediction_history
    """)

    avg_confidence = cursor.fetchone()[0]

    conn.close()

    return {
        "total_predictions": total_predictions,
        "most_common_disease": most_common_disease,
        "average_confidence": round(avg_confidence, 2) if avg_confidence else 0
    }


if __name__ == "__main__":

    create_database()

    print("Database Ready")