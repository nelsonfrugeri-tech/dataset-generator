# LLM Gate - Your Gateway to Large Language Models
 
> This project serves as a gateway to interact with different Large Language Models (LLMs) like Azure OpenAI. It provides a standardized API for accessing LLM functionalities like text generation and image generation.

![image](https://images2.alphacoders.com/117/1177908.png)
 
### Key Features
 
* **Unified API:** Interact with multiple LLM providers through a single, consistent API.
* **Provider Abstraction:** Easily switch between LLM providers without modifying your core application logic.
* **Flexible and Extensible:**  Add support for new LLMs and functionalities through a well-defined interface.
* **Robust Error Handling:**  Provides informative error messages and handles various exception scenarios.
* **Built with FastAPI:**  Leverages FastAPI for high performance, automatic documentation (Swagger), and easy validation.
 
### Hexagonal Architecture Project
 
The project is organized into the following main components:
 
```
llm-gate/
├── src/
│   ├── api/
│   │   ├── adapter/
│   │   │   ├── cache/
│   │   │   │   └── simple/
│   │   │   ├── constant/
│   │   │   │   ├── api_version.py
│   │   │   ├── http/
│   │   │   │   └── v1/
│   │   │   │       ├── endpoint/
│   │   │   │       │   ├── chat_endpoint.py
│   │   │   │       │   ├── health_endpoint.py
│   │   │   │       │   ├── image_endpoint.py
│   │   │   │       │   ├── providers_endpoint.py
│   │   │   │       ├── header/
│   │   │   │       │   ├── embedding_header.py
│   │   │   │       └── payload/
│   │   │   │           ├── request/
│   │   │   │           │   ├── common_request.py
│   │   │   │           │   ├── chat_request.py
│   │   │   │           │   ├── image_request.py
│   │   │   │           └── response/
│   │   │   │               ├── chat_response.py
│   │   │   │               ├── error_response.py
│   │   │   │               ├── image_response.py
│   │   │   └── service/
│   │   │       └── provider/
│   │   │           ├── azure_openai/
│   │   │           │   ├── client/
│   │   │           │   │   └── azure_openai_client.py
│   │   │           │   └── domain/
│   │   │           │       ├── chat_completion.py
│   │   │           │       ├── image_generate.py
│   │   │           │       ├── embedding.py
│   │   │           └── service_provider.py
│   ├── core/
│   │   ├── business/
│   │   │   ├── chat_business.py
│   │   │   ├── provider_business.py
│   │   │   └── embedding_business.py
│   │   ├── calculation/
│   │   │   ├── cost/
│   │   │   │   ├── text_cost.py
│   │   │   │   ├── image_cost.py
│   │   └── log/
│   │       └── middleware/
│   │           └── http_log_middleware.py
│   └── app.py
└── README.md
 
```
 
**src/api/adapter**
Contains adapters responsible for communicating with external APIs and services.
***src/api/adapter/cache:*** Implements caching mechanisms used to store temporary information such as provider and model data.
***simple/provider_cache.py:*** Manages the cache for provider information, improving performance by avoiding repeated API calls for static data.
***src/api/adapter/constant:*** Stores project-wide constants.

**src/api/adapter/http/v1:** Handles HTTP requests and responses, and includes the versioned API endpoints.

**endpoint:** Contains individual API endpoints.
***chat_endpoint.py:*** Endpoint for managing chat-related operations, allowing users to interact with the LLM for conversation-based tasks.
***health_endpoint.py***: Provides the health check for the API, ensuring the system is running properly.
***image_endpoint.py:*** Handles requests for image generation via LLM models like DALL·E.
***providers_endpoint.py:*** Lists available LLM providers and models, allowing users to dynamically select and switch between them.

**header:** Defines the headers required for API requests.
***embedding_header.py***: Specific header definitions for embedding-related API requests.

**payload:** Manages request and response payload models.
**request:** Defines the structure for incoming API requests.
***common_request.py:*** Contains common request parameters and structure.
***chat_request.py:*** Request model for chat-based interactions with the LLM.
***image_request.py:*** Request model for image generation tasks.
**response:** Defines the structure for outgoing API responses.
***chat_response.py:*** Model for returning chat responses from the LLM.
***error_response.py:*** Handles error responses, standardizing how errors are communicated to the client.
***image_response.py:*** Model for returning image generation results.

**src/api/adapter/service**
Handles provider-specific integrations.

**azure_openai:** Azure OpenAI implementation for interacting with Azure's OpenAI services.
***client/azure_openai_client.py:*** Client for communicating with Azure OpenAI APIs, abstracting the interaction logic.
***domain/chat_completion.py:*** Logic for handling chat completion tasks within Azure OpenAI.
***domain/image_generate.py:*** Manages image generation requests within Azure OpenAI.
***domain/embedding.py:*** Manages embedding-related tasks, allowing the system to generate embeddings from text.
***service_provider.py:*** Core service provider logic that manages the integration and communication with various LLM providers.

**src/core**
Contains the core business logic and domain models.

**business:** Implements the main business logic of the application.
***chat_business.py:*** Manages chat-related business operations, coordinating requests to LLMs for conversations.
***provider_business.py:*** Handles business logic related to managing and listing LLM providers and models.
***cost_business.py:*** Manages the business logic for calculating the costs of various LLM services based on usage.
***embedding_business.py:*** Business logic related to embedding operations, such as generating and retrieving text embeddings.

**calculation/cost:** Contains logic for calculating usage costs.
***text_cost.py:*** Handles cost calculations for text-based LLM interactions, factoring in tokens used.
***image_cost.py***: Manages cost calculations for image generation tasks based on pixel count and image quality.

**log/middleware:** Implements logging middleware for tracking and monitoring API requests.
***http_log_middleware.py:*** Middleware for logging HTTP requests, capturing important metrics and information for debugging and auditing.

**src/app.py**
The main entry point of the application, where the FastAPI server is initialized and configured.
 
### Getting Started
 
1. **Clone the repository:**
   ```bash
   git clone https://localiza@dev.azure.com/localiza/GenAI%20Aceleradores/_git/llm-gate
   cd llm-gate
   ```
 
2. **Set up the environment:**
   - Create a virtual environment: `python -m venv env`
   - Activate the environment: `source env/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
 
3. **Configure Environment Variables:**
    - Create a `.env` file in the root directory.
    - Add the following variables and replace placeholders with actual values:
        ```dotenv
        # HEIMDALL
        HEIMDALL_API_TITLE="HEIMDALL"
        HEIMDALL_API_DESCRIPTION="Responsible for being the application integration with GenAI models"
        HEIMDALL_API_PATH="/llm-gate"
        HEIMDALL_SERVER_HOST="0.0.0.0"
        HEIMDALL_SERVER_PORT="8080"

        # AZURE OPENAI
        AZURE_OPENAI_WEST_US_API_KEY=
        AZURE_OPENAI_WEST_US_ENDPOINT=
        AZURE_OPENAI_EAST_US_API_KEY=
        AZURE_OPENAI_EAST_US_ENDPOINT=

        #HttpClient
        HTTPX_CLIENT_VERIFY="False"

        #LOG
        LOG_LEVEL="INFO"
        ```
 
4. **Run the Application:**
   ```bash
   python src/api/app.py
   ```
   The application will be accessible at `http://localhost:8080/llm-gate/docs` (Swagger UI).
 
### Usage
 
#### Make a Chat Request
 
 ## Providers

**Description:** This endpoint retrieves a list of all available LLM providers and the models they support. It helps users identify which models they can use for various GenAI tasks, such as text generation, embeddings, and image generation.

Purpose:

The /providers endpoint is designed to give users an overview of the available Large Language Model (LLM) providers and the specific models they offer.
This allows developers and systems to choose from the available models depending on their requirements (e.g., text generation, embeddings, or other AI tasks).
By retrieving this information dynamically, the system remains flexible, allowing for new providers or models to be added without changing the API interface.

**Endpoint:** `/llm-gate/v1/providers`
 
**Method:** `GET`

**Request Headers:**
- `X-Correlation-Id`:  (Required) A UUID to correlate requests.
- `X-User-Id`: (Required) An identifier for the user making the request.
- `client_id`: (Required) Client application identifier.

**Response Body:**
```json
{
    "data": [
        {
            "id": "3b276615-51e7-4f05-ae95-4bf4fc6f99bb",
            "name": "azure_openai",
            "label": "Azure OpenAI",
            "description": "Azure OpenAI provider",
            "model": [
                {
                    "id": "b5be3878-8293-4646-9d99-e61d76859246",
                    "name": "gpt-35-turbo",
                    "label": "GPT-3.5 Turbo",
                    "description": "GPT-3.5 Turbo model",
                    "contextWindow": 16385,
                    "tranningData": "Sep 2021",
                    "enabled": true
                },
                {
                    "id": "c722f86c-fba3-4afc-8fce-c3c0b01adef9",
                    "name": "gpt-4",
                    "label": "GPT-4",
                    "description": "GPT-4 model",
                    "contextWindow": 8192,
                    "tranningData": "Sep 2021",
                    "price": [
                        {
                            "id": "edce6bf3-7e9a-4e63-8ed2-34e27791be94",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "token": {
                                "inputValue": 30.0,
                                "outputValue": 60.0
                            }
                        }
                    ],
                    "enabled": true
                },
                {
                    "id": "c51a6ccf-d087-48f3-853d-a70ba5d1bc58",
                    "name": "dall-e-2",
                    "label": "DALL·E-2",
                    "description": "DALL·E-2 model for image generation",
                    "tranningData": "Nov 2022",
                    "price": [
                        {
                            "id": "d4abfd11-f41f-4b8c-b5cd-94fdba9edce2",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1024,
                                "height": 1024,
                                "value": 0.02
                            }
                        },
                        {
                            "id": "f59511f8-c7df-4beb-b7d6-0cd1491fccd8",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 512,
                                "height": 512,
                                "value": 0.018
                            }
                        },
                        {
                            "id": "204646f5-5345-4022-b6ad-dba5b5de5577",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 256,
                                "height": 256,
                                "value": 0.016
                            }
                        }
                    ],
                    "enabled": true
                },
                {
                    "id": "cb11cbd3-4632-4e4c-8f0d-b328e2f8cb1f",
                    "name": "dall-e-3",
                    "label": "DALL·E-3",
                    "description": "DALL·E-3 model for advanced image generation",
                    "tranningData": "Nov 2023",
                    "price": [
                        {
                            "id": "3e7d76d9-0c44-427a-b2b9-86547d6e423a",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1024,
                                "height": 1024,
                                "quality": "Standard",
                                "value": 0.04
                            }
                        },
                        {
                            "id": "8b68b9d1-574c-4f2c-82de-a543ce12a560",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1792,
                                "height": 1024,
                                "quality": "Standard",
                                "value": 0.08
                            }
                        },
                        {
                            "id": "133d9a69-0b11-49b0-8bb4-21c9b4b0b653",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1024,
                                "height": 1024,
                                "quality": "HD",
                                "value": 0.08
                            }
                        },
                        {
                            "id": "87f4759a-30de-4eb1-9121-3b311a56cd01",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1792,
                                "height": 1024,
                                "quality": "HD",
                                "value": 0.12
                            }
                        }
                    ],
                    "enabled": true
                },
                {
                    "id": "55eead83-9eef-4117-bb8a-76034b3ea965",
                    "name": "gpt-4o",
                    "label": "GPT-4o",
                    "description": "GPT-4 multimodal",
                    "contextWindow": 128000,
                    "tranningData": "Oct 2023",
                    "price": [
                        {
                            "id": "fd028109-ce01-449e-8d57-9ce8b0bd18f0",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "token": {
                                "inputValue": 5.0,
                                "outputValue": 15.0
                            }
                        },
                        {
                            "id": "f033eaae-469e-424f-ab92-f21070b1b169",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1024,
                                "height": 1024,
                                "quality": "Standard",
                                "value": 0.003825
                            }
                        }
                    ],
                    "enabled": true
                },
                {
                    "id": "e8ba3ebd-c3fe-4392-9b79-b3890ad58a8a",
                    "name": "gpt-4o-mini",
                    "label": "GPT-4 Mini",
                    "description": "GPT-4 Smaller Variant",
                    "contextWindow": 64000,
                    "tranningData": "Oct 2023",
                    "price": [
                        {
                            "id": "980f4e53-a5bd-48ca-869f-7b81f9a69c4b",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "token": {
                                "inputValue": 0.15,
                                "outputValue": 0.6
                            }
                        },
                        {
                            "id": "34c7c489-7f7d-45dd-8f5a-219e4fd95a6f",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "pixel": {
                                "width": 1024,
                                "height": 1024,
                                "quality": "Standard",
                                "value": 0.003825
                            }
                        }
                    ],
                    "enabled": true
                },
                {
                    "id": "ea163644-56db-498a-9705-b3c831389320",
                    "name": "text-embedding-ada-002",
                    "label": "Text Embedding Ada 002",
                    "description": "Ada 002 for embedding",
                    "price": [
                        {
                            "id": "cd104459-6fd0-4546-9dbb-d35ea36344a7",
                            "unitOfMeasure": 1000000,
                            "currency": "USD",
                            "token": {
                                "inputValue": 0.1
                            }
                        }
                    ],
                    "enabled": true
                }
            ]
        }
    ]
}
```

## Chat

**Endpoint:** `/llm-gate/v1/chat`
 
**Method:** `POST`
 
**Headers:**
- `X-Correlation-Id`:  (Required) A UUID to correlate requests.
- `X-User-Id`: (Required) An identifier for the user making the request.
- `client_id`: (Required) Client application identifier.
 
**Request Body:**
```json
{
  "provider": {
    "name": "azure_openai",
    "model": {
      "name": "gpt-35-turbo" 
    }
  },
  "prompt": {
    "parameter": {
      "temperature": 0.7, 
      "maxTokens": 50 
    },
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you?"
      }
    ]
  }
}
```
 
**Response Body:**
```json
{
  "usage": {
    "completionTokens": 5,
    "promptTokens": 8,
    "totalTokens": 13
  },
  "messages": [
    {
      "role": "assistant",
      "content": "I am doing well, thank you. How can I assist you today?"
    }
  ]
}
```
 
#### Make an Image Generation Request
 
**Endpoint:** `/llm-gate/v1/images/generations`
 
**Method:** `POST`
 
**Headers:**
- `X-Correlation-Id`:  (Required) A UUID to correlate requests.
- `X-User-Id`: (Required) An identifier for the user making the request.
- `client_id`: (Required) Client application identifier.
 
**Request Body:**
```json
{
  "provider": {
    "name": "azure_openai",
    "model": {
      "name": "dall-e-2" 
    }
  },
  "prompt": {
    "message": "A cat wearing a hat", 
    "parameter": {
      "n": 1, 
      "size": "1024x1024" 
    }
  }
}
```
 
**Response Body:**
```json
{
  "data": [
    {
      "url": "https://example.com/generated_image.png" 
    }
  ]
}
```
 
 
### Contributing
 
We welcome contributions! If you'd like to contribute to the project, please follow these steps:
 
1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Make your changes and commit them.**
4. **Push your changes to your fork.**
5. **Submit a pull request.**
 
 
### License
 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.