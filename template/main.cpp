#include "template.hpp"
#include <libdnf5-cli/session.hpp>

int main(int argc, char *argv[]) {
    try {
        libdnf5::cli::session::Session session;
        dnf5::TemplateCommand template_cmd(session);
        session.register_subcommand(std::make_unique<dnf5::TemplateCommand>(session));

        return session.run(argc, argv);
    } catch (const std::exception & ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }
}
