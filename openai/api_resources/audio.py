from typing import Any, List, Optional, IO

import openai
from openai import api_requestor, util
from openai.api_resources.abstract import APIResource


class Audio(APIResource):
    OBJECT_NAME = "audio"

    @classmethod
    def _get_url(cls, action: str) -> str:
        return cls.class_url() + f"/{action}"

    @classmethod
    def _prepare_request(
        cls,
        file: IO,
        filename: str,
        model: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=api_base or openai.api_base,
            api_type=api_type,
            api_version=api_version,
            organization=organization,
        )
        files: List[Any] = []
        data = {
            "model": model,
            **params,
        }
        files.append(("file", (filename, file, "application/octet-stream")))
        return requestor, files, data

    @classmethod
    def transcribe(
        cls,
        model: str,
        file: IO,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, model, **params)
        url = cls._get_url("transcriptions")
        response, _, api_key = requestor.request("post", url, files=files, params=data)
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    def translate(
        cls,
        model: str,
        file: IO,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, model, **params)
        url = cls._get_url("translations")
        response, _, api_key = requestor.request("post", url, files=files, params=data)
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    def transcribe_raw(
        cls,
        model: str,
        file: IO,
        filename: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, filename, model, **params)
        url = cls._get_url("transcriptions")
        response, _, api_key = requestor.request("post", url, files=files, params=data)
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    def translate_raw(
        cls,
        model: str,
        file: IO,
        filename: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, filename, model, **params)
        url = cls._get_url("translations")
        response, _, api_key = requestor.request("post", url, files=files, params=data)
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    async def atranscribe(
        cls,
        model: str,
        file: IO,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, model, **params)
        url = cls._get_url("transcriptions")
        response, _, api_key = await requestor.arequest(
            "post", url, files=files, params=data
        )
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    async def atranslate(
        cls,
        model: str,
        file: IO,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, model, **params)
        url = cls._get_url("translations")
        response, _, api_key = await requestor.arequest(
            "post", url, files=files, params=data
        )
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    async def atranscribe_raw(
        cls,
        model: str,
        file: IO,
        filename: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, filename, model, **params)
        url = cls._get_url("transcriptions")
        response, _, api_key = await requestor.arequest(
            "post", url, files=files, params=data
        )
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )

    @classmethod
    async def atranslate_raw(
        cls,
        model: str,
        file: IO,
        filename: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        **params,
    ):
        requestor, files, data = cls._prepare_request(file, filename, model, **params)
        url = cls._get_url("translations")
        response, _, api_key = await requestor.arequest(
            "post", url, files=files, params=data
        )
        return util.convert_to_openai_object(
            response, api_key, api_version, organization
        )
