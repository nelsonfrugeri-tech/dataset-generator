import os
from pathlib import Path


def read_md_file(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()


def split_by_topics(content: str) -> list:
    chunks = []
    current_chunk = []

    lines = content.split("\n")
    for line in lines:
        if line.startswith("#"):
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
        current_chunk.append(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


def save_chunks(chunks: list, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(output_dir, f"chunk_{i+1}.txt")
        with open(chunk_path, "w") as f:
            f.write(chunk)


def chunk_md_file(input_path: str, output_dir: str):
    content = read_md_file(input_path)
    chunks = split_by_topics(content)
    save_chunks(chunks, output_dir)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_md_file = os.path.join(base_dir, "file", "source", "README.md")
    output_dir = os.path.join(base_dir, "file", "chunk")

    chunk_md_file(input_md_file, output_dir)
