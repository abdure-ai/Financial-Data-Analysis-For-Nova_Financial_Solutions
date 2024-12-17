import pandas as pd

def load_file(file_path):
    """
    Load a file into a pandas DataFrame.
    
    Supported formats:
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    - JSON (.json)

    Parameters:
    file_path (str): Path to the file.

    Returns:
    pd.DataFrame: Loaded DataFrame.
    """
    try:
        # Determine the file format from the extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv, .xlsx, .xls, or .json file.")
        
        print(f"File '{file_path}' loaded successfully.")
        return df

    except Exception as e:
        print(f"Error loading file: {e}")
        return None
