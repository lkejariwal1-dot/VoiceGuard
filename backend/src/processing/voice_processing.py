import os
from backend.src.utilis.logger import logger
from df.enhance import enhance, init_df, load_audio, save_audio


def enhance_audio(input_audio: str, output_audio: str) -> None:
    """
    Enhance an audio file using DeepFilterNet and save the result.
    """

    try:
        # ------------------------------------------------------------
        # 1. Validate input
        # ------------------------------------------------------------

        logger.info("Starting audio enhancement")
        logger.info("Input audio: %s", input_audio)

        if not os.path.isfile(input_audio):
            logger.error("Input audio file not found: %s", input_audio)
            raise FileNotFoundError(
                f"Input audio file not found: {input_audio}"
            )

        # Make sure output directory exists
        output_dir = os.path.dirname(output_audio)

        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # ------------------------------------------------------------
        # 2. Load DeepFilterNet
        # ------------------------------------------------------------
        model, df_state, _ = init_df()


        # ------------------------------------------------------------
        # 3. Load input audio
        # ------------------------------------------------------------
        audio, _ = load_audio(
            input_audio,
            sr=df_state.sr()
        )

        # ------------------------------------------------------------
        # 4. Enhance audio
        # ------------------------------------------------------------
        enhanced_audio = enhance(
            model,
            df_state,
            audio
        )

        # ------------------------------------------------------------
        # 5. Save enhanced audio
        # ------------------------------------------------------------
        save_audio(
            output_audio,
            enhanced_audio,
            df_state.sr()
        )

        logger.info(
            "Enhanced audio saved successfully: %s",
            output_audio
        )

    except Exception:
        logger.exception("Audio enhancement failed")
        raise
