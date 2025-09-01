# Onde Está Meu Caramelo? 🐾

## Sobre o Projeto

**Onde Está Meu Caramelo?** é um projeto inovador desenvolvido por estudantes da Universidade de Brasília (UnB) com a missão de reunir cães perdidos a seus tutores no Distrito Federal através do uso de inteligência artificial.

A dor de perder um animal de estimação é imensa. Nossa plataforma busca amenizar essa angústia, oferecendo uma ferramenta tecnológica e colaborativa para localizar pets desaparecidos. O sistema utiliza uma Inteligência Artificial para realizar o reconhecimento facial de cães, analisando características únicas do rosto e, principalmente, do focinho de cada animal.

Quando um usuário encontra um cão perdido, ele pode tirar uma foto e enviá-la para a nossa plataforma. A IA então compara essa imagem com o nosso banco de dados de cães desaparecidos. Se uma correspondência for encontrada, o tutor é notificado imediatamente com a possível localização de seu amigo de quatro patas.

Este projeto foi destaque em uma reportagem da [Globo](https://globoplay.globo.com/v/13687647/), que detalha nossa motivação e o funcionamento da tecnologia.

## ✨ Como Funciona

O coração do nosso projeto é uma Rede Neural Siamesa, um tipo de arquitetura de inteligência artificial especializada em aprender similaridades. Diferente de um modelo de classificação tradicional que tentaria identificar a raça de um cão, nosso sistema aprende a determinar se duas imagens pertencem ao mesmo animal.

O processo funciona da seguinte forma:

1. Treinamento com Triplets: O modelo é treinado com um método chamado Triplet Loss. Para cada imagem de referência (a "âncora"), ele analisa uma segunda foto do mesmo cão (a "positiva") e uma foto de um cão diferente (a "negativa"). O objetivo é que a rede aprenda a gerar representações matemáticas (embeddings) que minimizem a distância entre a âncora e a positiva, e maximizem a distância entre a âncora e a negativa.

2. Cálculo da Pontuação de Semelhança: Com o modelo treinado, ele se torna capaz de comparar duas imagens de cães que nunca viu antes e gerar uma pontuação de semelhança. Essa pontuação indica a probabilidade de as duas fotos serem do mesmo cão.

Notificação: Se a pontuação de semelhança entre a foto do cão encontrado e um dos cães perdidos for suficientemente alta, o tutor é notificado com a possível localização para o resgate.

## 🚀 Estágio Atual do Projeto

Atualmente, o projeto está em fase de **desenvolvimento e treinamento do modelo de IA**. O maior desafio é construir um banco de dados robusto e diversificado de imagens de cães para garantir a precisão do nosso algoritmo.

**O aplicativo ainda não está disponível para o público.** A fase atual é focada exclusivamente na coleta de dados.

-----