from fastapi import APIRouter
from .. import config, schema

router = APIRouter(prefix="/data")


@router.get("/about_me", response_model=schema.AboutMe)
async def get_about_me():
    return schema.AboutMe(
        **(await config.db.get_collection("AboutMe").find().to_list(None))[0]
    )


@router.get("/certificates", response_model=schema.Certificates)
async def get_certificates():
    return schema.Certificates(
        certificates=await config.db.get_collection("Certificates").find().to_list(None)
    )


@router.get("/experience", response_model=schema.Experiences)
async def get_experience():
    return schema.Experiences(
        experiences=await config.db.get_collection("Experience").find().to_list(None)
    )


@router.get("/projects", response_model=schema.Projects)
async def get_projects():
    return schema.Projects(
        projects=await config.db.get_collection("Projects").find().to_list(None)
    )


@router.get("/skills", response_model=schema.Skills)
async def get_skills():
    return schema.Skills(
        **(await config.db.get_collection("Skills").find().to_list(None))[0]
    )


@router.get("/social", response_model=schema.Socials)
async def get_social():
    return schema.Socials(
        socials=await config.db.get_collection("SocialNetworks").find().to_list(None)
    )


@router.get("/typing", response_model=schema.Typings)
async def get_typing():
    return schema.Typings(
        typing=await config.db.get_collection("Typing").find().to_list(None)
    )
