import os
from pathlib import Path
from llm.openai_client import OpenAIClient


class DatasetSwaggerGenerator:
    def __init__(self):
        self.client = OpenAIClient()

    def generate_dataset(self):
        swagger_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "file", "source", "swagger.json"
        )

        with open(swagger_file, 'r', encoding='utf-8') as file:
            swagger_content = file.read()

        print(f"SWAGGER FILE: {swagger_content}")

        prompt = (
                "Você é um gerador de datasets. Sua tarefa é criar datasets de mensagens de chatbot conversacionais. "
                "Obrigatoriamente o formato das suas respostas são em JSON utilizando a seguinte estrutura: "
                '{"datasets": ['
                '{"messages": ['
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                ']}]}'
                f"Entenda profundamente o contrato de API, cada endpoint e seu propósito: {swagger_content}."
                "Seu objetivo é gerar 30 perguntas e respostas para cada endpoint do LLM Gate, simulando uma conversa entre um desenvolvedor de software e um chatbot Copilot que tem total conhecimento do contrato de API da aplicação LLM Gate. "
                "Simule perguntas e respostas para cada endpoint fornecido pelo contrato de API, o desenvolvedor vai querer ver exemplos de cURL para usar um endpoint, vai querer saber o que cada parâmetro significa, vai fazer perguntas relacionadas aos contratos de API e você deve gerar essas perguntas e respostas simulando uma conversa real. "
                "Simulate questions and answers for each endpoint provided by the API, the developer will want to see cURL examples to use an endpoint, will want to know what each parameter means, will ask questions related to the application's API contracts and you should generate these questions and answers simulating a real conversation."
                "As perguntas e respostas devem ser escritas em português do Brasil, e você deve evitar traduzir nomes próprios, termos técnicos e jargões de desenvolvimento de software."
        )
                      
        messages = [
            {
                "role": "system",
                "content": prompt,
            },
            {"role": "user", "content": swagger_content},
        ]

        response = self.client.generate_text(
            messages,
        )

        print(f"Generator README *** Response LLM: {response}")

        self.save_dataset(
            response,
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "file",
                "dataset",
                "epoch_III",
                f"dataset_swagger.json",
            ),
        )

    def save_dataset(self, response, output_file: str):
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as f:
            f.write(f"{response}\n\n")

        print(f"Save dataset: {output_file}")


class DatasetReadmeGenerator:
    def __init__(self, chunk_dir: str):
        self.client = OpenAIClient()
        self.chunk_dir = chunk_dir

    def read_chunks(self):
        chunk_files = Path(self.chunk_dir).glob("*.txt")
        chunks = []
        for chunk_file in chunk_files:
            with open(chunk_file, "r") as file:
                chunks.append(file.read())
                print(f"Read chunk file: {chunk_file}")
        return chunks

    def generate_dataset(self):
        swagger_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "file", "source", "swagger.json"
        )

        with open(swagger_file, 'r', encoding='utf-8') as file:
            swagger_content = file.read()

        chunks = self.read_chunks()

        prompts = {
            "onboarding_developer": (
                "Você é um gerador de datasets. Sua tarefa é criar datasets de mensagens de chatbot conversacionais. "
                "Obrigatoriamente o formato das suas respostas são em JSON utilizando a seguinte estrutura: "
                '{"dataset": ['
                '{"messages": ['
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                ']}]}'
                f"Entenda profundamente o contrato de API, cada endpoint e seu propósito: {swagger_content}."
                "Seu objetivo é gerar 30 perguntas e respostas para o conteúdo fornecido, simulando uma conversa entre um desenvolvedor de software e um chatbot Copilot que tem total conhecimento do projeto LLM Gate. "                
                "Simule perguntas e respostas para cada endpoint fornecido pelo projeto, o desenvolvedor vai querer ver exemplos de cURL para usar um endpoint, vai querer saber o que cada parâmetro significa, vai fazer perguntas relacionadas aos contratos de API do LLM Gate e você deve gerar essas perguntas e respostas simulando uma conversa real. "
                "Crie diversos cenários de perguntas e respostas, desde conversas mais simples até diálogos complexos, simulando diferentes tipos de perguntas que um desenvolvedor de software faria para um chatbot Copilot que tem total conhecimento do LLM Gate."
                "As perguntas e respostas devem ser escritas em português do Brasil, e você deve evitar traduzir nomes próprios, termos técnicos e jargões de desenvolvimento de software."
            ),
            "usecase_question": (
                "Você é um gerador de datasets. Sua tarefa é criar datasets de mensagens de chatbot conversacionais. "
                "Obrigatoriamente o formato das suas respostas são em JSON utilizando a seguinte estrutura: "
                '{"dataset": ['
                '{"messages": ['
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                '{"role": "user", "content": "Aqui vai a pergunta do usuário"}, '
                '{"role": "assistant", "content": "Resposta da LLM"}, '
                ']}]}'
                f"Entenda profundamente o contrato de API, cada endpoint e seu propósito: {swagger_content}."
                "Seu objetivo é gerar 30 perguntas e respostas para o conteúdo fornecido, simulando uma conversa entre um usuário cliente da aplicação e um chatbot Copilot que tem total conhecimento do projeto. "                
                "Simule perguntas e respostas para cada endpoint fornecido pelo projeto, o usuário cliente vai querer ver exemplos de cURL para usar um endpoint, vai querer saber o que cada parâmetro significa, vai fazer perguntas relacionadas aos contratos de API do projeto, vai querer entender o que cada endpoint faz e como eles funcionam, com isso você deve entender cada endpoint profudamente em seus propósitos e funcionalidades para orientar o usuário, você deve gerar essas perguntas e respostas simulando uma conversa real. "
                "Crie diversos diálogos, desde conversas com perguntas e resposas simples até conversas mais complexas, simulando um usuário cliente que está conhecendo o projeto e quer entender como ele funciona. "
                "As perguntas e respostas devem ser escritas em português do Brasil, e você deve evitar traduzir nomes próprios, termos técnicos e jargões de desenvolvimento de software."
            ),
        }
        
        for key in prompts:            
            count = 1
            for chunk in chunks:                
                messages = [
                    {
                        "role": "system",
                        "content": prompts[key],
                    },
                    {"role": "user", "content": chunk},
                ]

                response = self.client.generate_text(
                    messages,
                )

                print(f"Generator README *** Response LLM: {response}")

                self.save_dataset(
                    response,
                    os.path.join(
                        os.path.dirname(os.path.abspath(__file__)),
                        "file",
                        "dataset",
                        "epoch_III",
                        f"dataset_{key}_{count}.json",
                    ),
                )
                count += 1

    def save_dataset(self, response, output_file: str):
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as f:
            f.write(f"{response}\n\n")

        print(f"Save dataset: {output_file}")


if __name__ == "__main__":
    generator_readme = DatasetReadmeGenerator(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", "chunk")
    )
    generator_readme.generate_dataset()

    generator_swagger = DatasetSwaggerGenerator()
    generator_swagger.generate_dataset()
