#pragma once

#include <torch/types.h>
#include "image_read_mode.h"

namespace vision {
namespace image {

C10_EXPORT torch::Tensor decode_jpeg_cuda(
    const torch::Tensor& data,
    ImageReadMode mode);
//    torch::Device device);
//C10_EXPORT torch::Tensor decode_jpeg_cuda(
//    const torch::Tensor& data,
//    ImageReadMode mode);

C10_EXPORT torch::Tensor read_file(const std::string& filename);

} // namespace image
} // namespace vision
