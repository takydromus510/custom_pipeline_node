
from nodes import BaseNode, CustomNode

class CustomPipelineNode(CustomNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sampler": ("SAMPLER",),
                "noise": ("NOISE",),
                "latent": ("LATENT",),
                "vae": ("VAE",),
                "model": ("MODEL",),
                "sigmas": ("SIGMAS",),
                "conditioning1": ("CONDITIONING",),
                "conditioning2": ("CONDITIONING",)
            }
        }

    RETURN_TYPES = ("SAMPLER", "NOISE", "LATENT", "VAE", "MODEL", "SIGMAS", "CONDITIONING", "CONDITIONING")
    FUNCTION = "pass_through"
    CATEGORY = "Pipelines"

    def pass_through(self, sampler, noise, latent, vae, model, sigmas, conditioning1, conditioning2):
        """
        Simply passes the input data sets to the output without modification.
        """
        return sampler, noise, latent, vae, model, sigmas, conditioning1, conditioning2
