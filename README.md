# SPDX-OSS-Dataset

## Description

To implement any Machine learning/Deep learning algorithm we need a better and bigger dataset of SPDX Licences. But unfortunately, there exists no such dataset for open source licenses on the web.

## Implementation

To generate the dataset the base approach we used is to n-gram the paragraphs of license texts and to generate different permutations and combinations of them Suppose a license text has 5 paragraphs [1,2,3,4,5] in order. To create a dataset we include subsets like [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] for all combinations starting from 1,2,3,4 and 5. each one with the same label.

Using this technique we were able to generate more than 1 million files from 447 SPDX license files.

Now, as all the para are not equally important and most of these will create a lot of noise in the dataset. To resolve this, we'll be choosing para with high relevance and then will repeat the same process.
