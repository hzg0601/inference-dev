.. _models_llm_internlm-20b:

========================================
internlm-20b
========================================

- **Context Length:** 16384
- **Model Name:** internlm-20b
- **Languages:** en, zh
- **Abilities:** generate
- **Description:** Pre-trained on over 2.3T Tokens containing high-quality English, Chinese, and code data.

Specifications
^^^^^^^^^^^^^^


Model Spec 1 (pytorch, 20 Billion)
++++++++++++++++++++++++++++++++++++++++

- **Model Format:** pytorch
- **Model Size (in billions):** 20
- **Quantizations:** 4-bit, 8-bit, none
- **Model ID:** internlm/internlm-20b

Execute the following command to launch the model, remember to replace ``${quantization}`` with your
chosen quantization method from the options listed above::

   xinference launch --model-name internlm-20b --size-in-billions 20 --model-format pytorch --quantization ${quantization}

